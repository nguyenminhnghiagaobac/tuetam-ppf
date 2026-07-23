# Bot Telegram @TueTamPPF_bot — Hướng dẫn cài (5 phút)

Bot chính thức của tiệm: vừa **trả lời tin nhắn** khách + anh Tân (AI Gemini),
vừa **chủ động nhắn anh Tân mỗi ngày 1 lần**. Đã chống spam sẵn. Chạy 24/7 miễn phí.

File code: [`troly-tuetam.gs.txt`](./troly-tuetam.gs.txt)

## 1. Lấy 2 khóa
- **BOT_TOKEN**: nhắn [@BotFather](https://t.me/BotFather) → `/newbot` (hoặc `/token` nếu đã có @TueTamPPF_bot).
- **GEMINI_KEY**: lấy miễn phí tại https://aistudio.google.com/apikey

## 2. Dán code vào Google Apps Script
1. Vào https://script.google.com → **New project**.
2. Xóa hết trong `Mã.gs`, dán toàn bộ nội dung `troly-tuetam.gs.txt`.
3. Điền `BOT_TOKEN` và `GEMINI_KEY` ở đầu file. `OWNER_CHAT_ID` đã điền sẵn (anh Tân).

## 3. Deploy (webhook để bot trả lời tin nhắn)
1. **Deploy → New deployment → Web app**.
2. *Execute as*: **Me** · *Who has access*: **Anyone** → **Deploy**.
3. Copy URL kết thúc bằng `/exec`.
4. Dán URL đó vào hàm `setWebhook` (biến `WEBAPP_URL`) → chọn hàm `setWebhook` → **Run** (cấp quyền lần đầu).
   > Đổi TOKEN hoặc Deploy bản mới (URL /exec đổi) thì chạy lại `setWebhook`.

## 4. Bật tin nhắn chủ động mỗi ngày
- Chọn hàm `setupTriggers` → **Run**. Mặc định nhắn anh Tân **1 lần lúc 8h sáng**.
- Muốn 2 lần/ngày: sửa `var GIO_NHAN = [8,18];` rồi chạy lại `setupTriggers`.
- Muốn tắt hẳn tự nhắn: đặt `var GIO_NHAN = [];` rồi chạy lại `setupTriggers`, hoặc chạy `xoaHetLich`.

## 5. Thử ngay
- Chạy hàm `guiThuNgay` → anh Tân nhận 1 tin thử ngay (không cần chờ tới sáng).
- Nhắn bot trong Telegram để kiểm tra phần trả lời.

## Lệnh trong Telegram (chỉ anh Tân dùng được)
| Lệnh | Tác dụng |
|------|----------|
| `/tat` | Ngưng tự nhắn mỗi ngày (bot vẫn trả lời khách) |
| `/bat` | Bật lại tự nhắn |
| `/trangthai` | Xem đang bật/tắt + số lịch đang chạy |

## Chống spam — có sẵn
- Tin chủ động **chỉ gửi cho anh Tân**, KHÔNG broadcast cho khách.
- Mặc định **1 tin/ngày**; chống trùng theo `update_id` và theo khung giờ.
- Khách bấm gửi dồn dập: mỗi khách chỉ được trả lời 1 câu / 4 giây (`KHACH_GIAN_CACH`).
