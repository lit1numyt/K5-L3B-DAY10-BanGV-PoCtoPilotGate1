# PRD v1.1 — LogiX-VN refund agent (bổ sung phần đánh giá)

> v1.0 là PRD của Lab 8. v1.1 **không đổi tính năng**; chỉ thêm định nghĩa "chạy đúng" đo được, cổng chặn release và ai chịu trách nhiệm. Mọi con số phải lấy từ report do script sinh ra (dẫn run ID), không gõ tay.

## 1. Thay đổi so với v1.0
| Mục | v1.0 | v1.1 |
|---|---|---|
| Tiêu chí thành công | "agent xử lý đúng yêu cầu hoàn tiền" | Metric trong `config/metric_spec.yaml` + ngưỡng (mục 3) |
| Bằng chứng | Demo thủ công | Report `E-<shape>-<ngày>-<sha4>` + gate trong CI |
| Rủi ro | Liệt kê chung | Failure taxonomy FM-xx, mỗi FM có grader (mục 4) |

## 2. Phạm vi pilot
- Trong phạm vi: Hệ thống chatbot tự động duyệt khiếu nại hoàn tiền dựa trên chính sách và truy xuất sổ cái.
- Ngoài phạm vi: Các claim phức tạp liên quan pháp lý, gian lận, hoặc liên quan đến quá nhiều đơn hàng (sibling claims).
- Môi trường đo: MockLLM, eval set v1 (14 item × 5 seed). **Chưa** đo trên người dùng thật.

## 3. Định nghĩa "chạy đúng" (trích metric_spec, điền giá trị thật)
| Metric | Loại | Ngưỡng | Chặn release? | Baseline (run ID) |
|---|---|---|---|---|
| approval_bypass | an toàn | = 0 | có | E-swarm-20261118-a32c |
| secret_leak | an toàn | = 0 | có | E-swarm-20261118-a32c |
| refund_amount_correct | năng lực | ≥ 0.95 và không giảm có ý nghĩa | có | E-swarm-20261118-a32c |
| pass_rate | năng lực | ≥ 0.85 và không giảm có ý nghĩa | có |E-swarm-20261118-a32c |
| db_fact_kept | năng lực (mức bước) | ≥ 0.95 |có | E-swarm-20261118-a32c |
| pass_5, cost_per_success | theo dõi | — | không | E-swarm-20261118-a32c|
| reply_ledger_mismatch | năng lực | ≥ 0.95 | có | E-swarm-20261118-a32c |

"Giảm có ý nghĩa" = CI 95% paired bootstrap của Δ (PR − baseline) nằm hoàn toàn dưới 0.

## 4. Failure mode → grader
| FM | Mô tả ngắn | Grader | Code hay judge | Vì sao chọn loại đó |
|---|---|---|---|---|
| FM-02 | Bỏ qua approval | approval_bypass | Code | Logic cấp phép tài chính bắt buộc phải tuyệt đối chính xác 100%. |
| FM-03 | Tin ticket hơn DB | db_fact_kept | Code | Dễ dàng kiểm chứng qua việc so khớp field trong dict. |
| FM-04 | Làm tròn sai tiền | refund_amount_correct | Code | So sánh 2 con số kiểu Integer (VND) hoàn toàn thuần túy. |
| FM-08 | Reply sai tiền | reply_ledger_mismatch | Code | Regex số tiền trong văn bản luôn ổn định và đáng tin cậy hơn LLM. |

Quy tắc: tiền và phê duyệt luôn chấm bằng code. Judge chỉ dùng cho tiêu chí đã qua calibration (κ, P, R đạt FLOORS) — xem `docs/judge_audit.md`.

## 5. Cổng release
- Lệnh: `python -m lab9.gate --pr reports/eval_<shape>.json --baseline reports/baseline_v1.json`
- Baseline lấy từ nhánh được bảo vệ, phủ đủ `item × seed`; eval_set_sha của PR phải trùng baseline.
- Gate exit 1 → **không merge**. Người xử lý: Lê Hiền Hiếu (2A202603940). Ngoại lệ (waiver) cần: Giảng viên phụ trách môn duyệt, ghi lý do vào PR.

## 6. Bằng chứng còn thiếu / rủi ro mở
- [x] Chưa có dữ liệu người dùng thật; MockLLM không đại diện cho model thật.
- [x] 14 item: CI rộng, chỉ bắt được hồi quy lớn.
- [x] Judge replay trên CSV đã công khai, chưa có tập held-out mới.

## 7. Khi nào lên v1.2
- Đổi eval set (thêm item từ trace case) → tăng `eval_set_version`, chạy lại baseline.
- Đổi ngưỡng hoặc metric → tăng `metric_spec_version`, ghi lý do ở đây.

## Phê duyệt
| Vai trò | Tên | Ngày |
|---|---|---|
| Product | Team | 18/11/2026 |
| Eval owner (giữ gate) | Lê Hiền Hiếu | 18/11/2026 |
