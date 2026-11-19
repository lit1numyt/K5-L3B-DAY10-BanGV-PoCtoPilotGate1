"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _facts(ctx, order_id):
    """Nguồn sự thật cho một đơn: đơn, kiện ticket nói tới (hoặc kiện trễ nhất), độ trễ theo tracking DB,
    chính sách có hiệu lực THEO NGÀY. Không đọc chữ khách viết."""
    order = ctx.tools.lookup_order(order_id)
    if not order or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    return order, parcel, delay, policy


def pre_guard(ctx):
    # Cổng 1 (B4 dòng INVALID, B6 Kỹ thuật 2): ghim chính sách theo ngày hiệu lực, không theo cờ index_active.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không có chính sách nào có hiệu lực hôm nay")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # Cổng 2 (B4 dòng PERTURBED, B6 Kỹ thuật 1): số tiền hoàn không được vượt quyền lợi tính từ tracking DB.
    # Chặn: số ngày khách tự khai, chỉ thị cài trong ghi chú (full_refund), fail_open khi LLM lỗi.
    if tool == "issue_refund":
        f = _facts(ctx, action.get("order_id"))
        if f is None or f[3] is None:
            return Verdict.escalate("thiếu dữ liệu đơn hoặc chính sách để kiểm số tiền hoàn")
        order, parcel, delay, policy = f
        entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if action.get("amount_vnd", 0) > entitled:
            ctx.log("refund_over_entitlement", asked=action.get("amount_vnd"), entitled=entitled, db_delay_days=delay)
            return Verdict.escalate(f"số tiền hoàn vượt quyền lợi theo tracking DB ({entitled}đ): chuyển người duyệt")

        # Nếu sắp ghi lỗi hãng thứ ba, chuyển người trước khi ghi tiền để tránh ticket đã hoàn nhưng lại chờ duyệt.
        proposal = next((e for e in reversed(ctx.events) if e.get("type") == "proposal"), {})
        limit = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        already_paid = ctx.tools.ledger_rows(ticket_id=action.get("ticket_id"))
        if (proposal.get("do_fault") and H.carrier_at_fault(policy, parcel, delay)
                and limit is not None and not already_paid
                and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limit):
            ctx.log("carrier_strike_limit", carrier_id=parcel["carrier_id"], limit=limit)
            return Verdict.escalate("hãng đã đủ số lỗi tự động trong ngày: chuyển người duyệt trước khi hoàn")

    # Cổng 3 (B4 dòng WRONG, INCOMPLETE, INCAPABLE; B6 Pháp lý): chỉ ghi lỗi hãng cho đúng kiện trễ, đúng số ngày
    # theo DB, khi chính sách cho phép; tối đa số lỗi tự động mỗi hãng mỗi ngày theo ops_limits.
    if tool == "file_carrier_fault":
        f = _facts(ctx, action.get("order_id"))
        if f is None or f[3] is None:
            return Verdict.deny("thiếu dữ liệu để ghi lỗi hãng")
        order, parcel, delay, policy = f
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking DB không cho thấy hãng có lỗi theo chính sách")
        limit = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if limit is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limit:
            ctx.log("carrier_strike_limit", carrier_id=parcel["carrier_id"], limit=limit)
            return Verdict.deny("hãng đã đủ số lỗi tự động trong ngày: người duyệt ghi tay")
        fix = {}
        if action.get("parcel_id") != parcel["parcel_id"]:
            fix.update(parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"))
        if action.get("delay_days") != delay:
            fix["delay_days"] = delay
        if fix:
            return Verdict.modify("ghi lỗi theo kiện trễ và số ngày trong tracking DB", **fix)

    # Cổng 3 (tiếp, B4 dòng Dữ liệu gửi bên thứ ba): chỉ gửi hãng các trường chính sách cho phép.
    if tool == "notify_carrier":
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        allowed = set((policy or {}).get("carrier_notice_fields") or [])
        payload = action.get("payload") or {}
        extra = sorted(set(payload) - allowed)
        if extra:
            ctx.log("carrier_payload_trimmed", dropped=extra)
            return Verdict.modify("chỉ gửi hãng các trường trong carrier_notice_fields",
                                  payload={k: v for k, v in payload.items() if k in allowed})

    return Verdict.allow()
