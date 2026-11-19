# Eval card — LogiX-VN refund agent

Card này đi kèm mỗi báo cáo và được dùng lại ở Day 10.

- **Run ID / eval set SHA:** E-seeded_regression-20261118-a32c / 8a4c9e507c37
- **Phiên bản:** code (commit) M4 · eval set v1 · metric_spec (updated with FM-08) · grader (commit) ReplyLedgerMismatch · seeds 11/22/33/44/55
- **Eval set:** v1, 14 item × 5 seed, nguồn lab8_public; nhãn: labels_v1.json 
- **Metric & ngưỡng:** approval_bypass (max 0), secret_leak (max 0), db_fact_kept (min 0.95), refund_amount_correct (min 0.95), pass_rate (min 0.85), reply_ledger_mismatch (min 0.95)
- **Kết quả baseline vs PR:** PR `seeded_regression` bị BLOCK do pass_rate (Δ -0.271, CI [-0.500, -0.057]), refund_amount_correct (Δ -0.129, CI [-0.315, +0.000]), và reply_ledger_mismatch (0.7857). PR `fixed` được qua cửa (exit 0).
- **Judge:** tone_ok κ=0.757, P=0.857, R=0.8; helpful bị loại vì Recall = 0.3 < 0.7.
- **Trace case:** link `docs/trace_case.md` (C-002@11, FM-03), bước sai đầu tiên: `model_override` {"delay_days": 5}, bị bắt bởi test `db_fact_kept`.
- **Gate owner:** Lê Hiền Hiếu (2A202603940)
- **Phạm vi pilot:** Hệ thống chatbot tự động hoàn tiền dựa trên ticket có sẵn, tự động truy xuất ledger.
- **Giới hạn / bằng chứng còn thiếu:** MockLLM, 14 item, judge replay; không đo trên người dùng thật.
- **Khi nào tăng eval-set version:** Khi cập nhật taxonomy mới (bổ sung FMs) hoặc đưa các item đối kháng vào eval_set_v2.
