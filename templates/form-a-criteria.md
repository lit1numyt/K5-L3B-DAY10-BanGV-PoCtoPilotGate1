# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-BanGV-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**

- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---



## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Xử lý khiếu nại giao hàng trễ theo chính sách có hiệu lực để khách nhận đúng khoản hoàn, với phê duyệt khi cần và số tiền thông báo cho khách khớp với giao dịch ghi trong sổ cái.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát: Mỗi kỳ đối soát tuần, số tiền trợ lý báo cho khách khớp đúng dòng sổ cái (PRD v1.1 §4, FM-08, metric `reply_ledger_mismatch`; eval card Lab 9 từng đo 0,7857, dưới ngưỡng 0,95), không có khoản hoàn nào chi khi thiếu phê duyệt hợp lệ (FM-02, `approval_bypass` = 0), và không có lỗi nào ghi oan cho hãng (hãng nhỏ GHSH bị phạt 150.000đ/lỗi, tạm ngưng sau 3 lỗi trong 7 ngày), để chị không phải sửa tay dòng nào và không hãng hay shop nào khiếu nại một khoản do trợ lý ghi sai.
- Chị Hạnh, trưởng ca CSKH: Mọi ca ngoài phạm vi pilot (claim pháp lý, nghi gian lận, nhiều đơn liên quan; PRD v1.1 §2) và mọi khoản vượt hạn mức đều được chuyển sang chị kèm lý do rõ ràng, nhưng tổng số ca chuyển trong một ca không vượt sức duyệt (1 người × 6 ca/giờ, `ops_facts`) và mỗi ca được nhận trong 60 phút (`ops_limits.review_sla_minutes`).

---



## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**

- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn số ngày giao trễ dùng để xét yêu cầu hoàn tiền. | Lệnh ghi file\_carrier\_fault: tác hại rơi vào hãng vận chuyển bên ngoài LogiX. PRD v1.1 §6 ghi chưa có dữ liệu người dùng thật và eval set chỉ 14 item, nên production là nơi duy nhất thấy tác hại thật |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ giữ đúng số ngày trễ theo dữ liệu vận chuyển (%). | Số lỗi trợ lý tự ghi cho mỗi hãng mỗi ngày (lỗi/hãng/ngày), kèm tỉ lệ lỗi bị hãng khiếu nại thắng trong 7 ngày lăn (%) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Toàn bộ ticket trong `data/tickets.jsonl` có thể đối chiếu đơn và kiện trong `data/world.json`; trace từng `ticket@seed` sau khi được phép đánh giá. Người đánh giá trong nhóm tính và gán nhãn số ngày trễ chuẩn từ ngày hẹn, ngày giao hoặc ngày mô phỏng. | Sổ lỗi hãng (carrier\_id, ngày, ticket, có nguyên nhân ghi trong tracking hay không) và khiếu nại hãng gửi về. Production không có nhãn: dùng khiếu nại thắng của hãng làm nhãn trễ, chị Oanh xác nhận khi đối soát tuần |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | 100 × số lần `delay_days_used` khớp nhãn chuẩn / tổng số lần có nhãn chuẩn; mỗi `ticket@seed` là một lần. Nếu ticket chỉ rõ kiện, lấy kiện đó; nếu không, lấy kiện trễ nhất. Độ trễ kiện = max(0, ngày giao − ngày hẹn), dùng ngày mô phỏng nếu chưa giao. Có nhãn nhưng thiếu `proposal` hoặc `delay_days_used`: tính không khớp và báo riêng. Không đủ dữ liệu gán nhãn: loại khỏi mẫu số và báo số lượng. | (1) Đếm số dòng file\_carrier\_fault do trợ lý ghi, nhóm theo carrier\_id và ngày. (2) Tỉ lệ khiếu nại thắng = số lỗi hãng khiếu nại thắng / tổng lỗi trợ lý ghi cho hãng đó trong 7 ngày; hãng chưa có lỗi nào thì ghi 0 lỗi, không tính tỉ lệ |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo ngày: hãng nào tới lỗi thứ 3 (vượt trần 2 lỗi tự động/hãng/ngày trong ops\_limits) thì báo NV-TUNG và chuyển lỗi đó cho người duyệt. Theo 7 ngày: GHSH có ≥ 2 lỗi, hoặc bất kỳ hãng nào có tỉ lệ khiếu nại thắng > 0%, thì báo đỏ và cân nhắc tắt file\_carrier\_fault |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không cho biết chính sách, số tiền hoàn hay ghi lỗi hãng có đúng không. Ca chuyển người duyệt trước `proposal` có thể an toàn nhưng vẫn bị tính không khớp; cần đọc cùng số ca thiếu. | Không thấy lỗi oan mà hãng không khiếu nại (hãng nhỏ ngại khiếu nại); khiếu nại về trễ nên báo động chậm; không thấy tác hại cho khách (hoàn thiếu tiền, FM-04) |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---



## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Y chỉ hơn X đúng 1 lần chạy (50/50 so với 49/50) và 1,0 của Y nằm trong khoảng tin cậy 95% [0,94; 1,0] của X, nên chưa đủ căn cứ nói Y tốt hơn; (a) sai vì chênh lệch không có ý nghĩa, (c) sai vì "chắc chắn như nhau" cũng không suy ra được, (d) sai vì chạy thêm seed chỉ làm khoảng tin cậy hẹp lại, không quyết định X đạt hay không.

---



## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate của trợ lý hoàn tiền trên bộ nền (22 ticket × 5 seed) tụt dưới **0,90** thì chúng tôi sẽ không chọn Tiếp tục; tìm kho/hãng có số xấu nhất và Thu hẹp phần đó. | Nếu pass_rate tụt dưới 0,85 (ngưỡng Lab 9) thì Cải tiến thêm. *Bỏ: Day 10 có lệnh ghi tiền thật, 0,85 quá lỏng.* |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 seed trên bộ nền tụt dưới **0,80** thì chúng tôi sẽ Thu hẹp: bỏ nhóm ticket chạy không ổn định khỏi phạm vi tự động, chuyển cho người duyệt. | — |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bộ nền hoặc gói sự cố vượt quá **0đ** thì chúng tôi sẽ không chọn Tiếp tục; sau 2 vòng sửa vẫn vượt thì tắt `issue_refund` tự động (stop_condition). | — |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục; sau 2 vòng sửa vẫn vượt thì tắt `file_carrier_fault`. | — |
| `pii_leaks_max` | Nếu số lần lộ dữ liệu cá nhân cho bên thứ ba vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục và chặn `notify_carrier` cho tới khi sửa. | — |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt quá **0,35** thì chúng tôi sẽ xem lại phạm vi: quá nhiều ca về tay chị Hạnh thì tự động hoá mất ý nghĩa và hàng chờ dễ vượt 60 phút. | — |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không bao giờ tự hoàn tiền theo số ngày trễ khách tự khai khi số đó khác tracking DB, và không bao giờ tự hoàn quá 300.000đ cho một khách trong ngày (`max_auto_refund_per_customer_per_day_vnd`).
- Ngưỡng chuyển cho người duyệt: chuyển cho chị Hạnh (NV-HANH) khi tổng hoàn tự động cho một khách vượt 300.000đ/ngày, khi một hãng sắp nhận lỗi thứ 3 trong ngày, hoặc khi ticket thuộc nhóm ngoài phạm vi (pháp lý, nghi gian lận, nhiều đơn liên quan, PRD §2).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | pass_rate/pass_k chủ yếu có ý nghĩa với khách và LogiX. Hãng và chị Oanh chỉ quan tâm 3 chỉ số an toàn (lỗi oan, hoàn sai), nên 3 chỉ số này đặt bằng 0. Chị Hạnh được bảo vệ bằng `escalation_rate_max` và `queue_stuck_max = 0`. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép pass_rate cao bằng cách chuyển hết cho người thì chị Hạnh gánh hàng chờ; ép escalation thấp thì hãng và khách gánh lỗi ghi sai. Vì vậy hai phía được giữ bằng hai ngưỡng ngược chiều. Chặn hết hay thu hẹp về 0 không được tính là đạt. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có: ngày 1 ở 2 kho, 1 người trực, dữ liệu mock (PRD §6). Ngày 1 ưu tiên "không ghi sai" hơn "tự động nhiều". |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải viết lại `escalation_rate_max` và `queue_stuck_max` theo số người trực thật; `cost_per_ticket_vnd_max` theo giá LLM thật; pass_rate phải đo lại trên dữ liệu thật vì chính sách đổi làm drift. 3 ngưỡng an toàn giữ bằng 0. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **6000** (thấp hơn rõ 10.000đ làm tay, chừa chỗ cho phí người duyệt 10.000đ/ca chuyển và 30.000đ phí giữ chỗ mỗi người trực) · `roi_min` **0,5** (mỗi đồng bỏ ra phải tiết kiệm ít nhất 0,5 đồng, sau khi trừ tiền hoàn sai) · `queue_stuck_max` **0** (`review_sla_minutes = 60`: không ca nào được chờ quá 60 phút)
- Ngày xem lại tiêu chí: `26/11/2026` (1 tuần sau Gate 1) · Ai dự: `Lê Hiền Hiếu (giữ gate), Đồng Hữu Nguyên Khoa (PIC vận hành), NV-HANH, NV-OANH` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---



## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục                                                                             | Điền      |
| ------------------------------------------------------------------------------- | --------- |
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-19T15:09:12 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`)      | e2cb911 |
| Đã push lên `origin main` thành công?                                           | có (15:09:58) |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
