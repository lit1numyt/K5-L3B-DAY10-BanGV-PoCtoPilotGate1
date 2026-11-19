"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def ledger_review_signals(trials):
    """Số lượt cổng phát hiện đã hoàn đủ, hoàn một phần hoặc thử ghi lặp."""
    kinds = {"refund_already_settled", "refund_remainder_adjusted", "refund_retry_blocked"}
    return sum(1 for trial in trials if any(
        event.get("type") == "guard" and event.get("kind") in kinds
        for event in trial.get("events", [])
    ))


def _review_cost_vnd():
    """Công người một ca chuyển duyệt, đọc từ data/world.json → ops_facts (nguồn số liệu chung, không gõ tay)."""
    import json
    from pathlib import Path
    try:
        facts = json.loads((Path(__file__).resolve().parent.parent / "data" / "world.json").read_text(encoding="utf-8"))["ops_facts"]
        return facts.get("review_cost_per_ticket_vnd", 10000), facts.get("recheck_with_note_units", 0.4)
    except Exception:
        return 10000, 0.4


def max_warehouse_cost_per_ticket(trials):
    """Chi phí xử lý bình quân mỗi ticket (tiền máy + công người duyệt) của KHO ĐẮT NHẤT, đồng/ticket.
    Ngưỡng: > 6.000đ (cost_per_ticket_vnd_max đã ký) là vàng; > 10.000đ (làm tay) là đỏ → thu hẹp kho đó."""
    review, recheck_units = _review_cost_vnd()
    by_wh = {}
    for t in trials:
        human = review if t.get("review_kind") == "escalated" else review * recheck_units if t.get("review_kind") == "recheck" else 0
        tot, n = by_wh.get(t.get("warehouse") or "?", (0, 0))
        by_wh[t.get("warehouse") or "?"] = (tot + (t.get("cost_vnd") or 0) + human, n + 1)
    return max((tot / n for tot, n in by_wh.values()), default=0.0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "ledger_review_signals": ledger_review_signals,
    "max_warehouse_cost_per_ticket": max_warehouse_cost_per_ticket,
}
STARTER_MONITORS = ("escalation_rate",)
