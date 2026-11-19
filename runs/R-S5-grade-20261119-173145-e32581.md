# Tự kiểm tra sự cố S5 · PASS-VISIBLE (chưa chạy test ẩn)

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S5-grade-20261119-173145-e32581` · bàn: `K5-L3B-DAY10-BanGV-PoCtoPilotGate1` · grader `lab10-1.0` · 2.199s
- Ba mốc: base `R-S5-before-20261119-173147-e32581` · prepared `R-S5-prepared-20261119-173147-e32581` · after `R-S5-after-20261119-173147-e32581` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `17287cf3`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `e325818ea0df`
- Hash Bản tiêu chí chấp nhận: `1f90c57a0d54` · đã ký: `1f90c57a0d54` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S5` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S5 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ✅ | file khoá bị đổi: không |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['ledger_review_signals', 'max_warehouse_cost_per_ticket']; sáng đèn: [('ledger_review_signals', 'after', 0.0, 25.0), ('max_warehouse_cost_per_ticket', 'before', 10359.0, 11325.666667), ('max_warehouse_cost_per_ticket', 'after', 10359.0, 820.5)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.4 | 0.5333 | 0.0 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 0 |
| chi phí mỗi ticket (đ) · làm tay | 6083 · 10000 | 6834 · 10000 | 2388 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 2412 · 1500 | 667 · 1500 | 1150 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -60486 | -58030 | 137007 |
| ROI | -0.33 | -0.28 | 3.19 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 196000 · 2000000 | 196000 · 2000000 | 98000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 178000 · 2000000 | 153000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 0.6 |
| số kho đắt hơn làm tay | 1 | 1 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 20 | 15 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.6667; hoàn sai 50000; oan 0; PII 0; chi phí 664đ | pass 0.6667; hoàn sai 50000; oan 0; PII 0; chi phí 664đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 664đ |
| kho DN | pass 0.8; hoàn sai 490000; oan 5; PII 0; chi phí 663đ | pass 0.8; hoàn sai 490000; oan 5; PII 0; chi phí 663đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 643đ |
| kho HCM | pass 0.5; hoàn sai 100000; oan 5; PII 0; chi phí 662đ | pass 0.5; hoàn sai 100000; oan 5; PII 0; chi phí 662đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 612đ |
| kho HCM-B2B | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 11326đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10382đ > làm tay | — |
| kho HN | pass 0.75; hoàn sai 250000; oan 10; PII 0; chi phí 1244đ | pass 0.875; hoàn sai 125000; oan 5; PII 0; chi phí 5477đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 820đ |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.8; hoàn sai 250000; oan 10; PII 0 | pass 0.9; hoàn sai 125000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 0.8333; hoàn sai 50000; oan 0; PII 0 | pass 0.8333; hoàn sai 50000; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.75; hoàn sai 590000; oan 10; PII 0 | pass 0.75; hoàn sai 590000; oan 10; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.2364 | 0.2364 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 0 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 4293 · 10000 | 4293 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 670 · 1500 | 670 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 125562 | 125562 |
| ROI | 1.34 | 1.33 | 1.33 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 1.0 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2967đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2967đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2364 | 0.2364 | +0.0091 |
| visible | pass_rate | 0.8333 | 0.8667 | 1.0 | +0.1667 |
| visible | pass_k | 0.8333 | 0.8667 | 1.0 | +0.1667 |
| visible | wrongful_refund_vnd | 890000 | 765000 | 0 | -890000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 20 | 15 | 0 | -20 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.4 | 0.5333 | 0.0 | -0.4 |
