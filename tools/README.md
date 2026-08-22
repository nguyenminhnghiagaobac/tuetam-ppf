# Bộ sinh nội dung tự động cho fanpage Tuệ Tâm PPF CNC

Scenario Make **"Tự động đăng bài Fanpage 8h & 17h"** mỗi ngày lấy đúng 2 file
trên website (Vercel) rồi đăng lên fanpage:

```
https://tuetamppf.vercel.app/media/lich/ppf-d{ngày}-{giờ}.png   → ảnh
https://tuetamppf.vercel.app/media/lich/ppf-d{ngày}-{giờ}.txt   → nội dung
```

`{ngày}` = ngày trong tháng (01…31), `{giờ}` = `08` hoặc `17`.
Muốn đổi bài đăng thì sửa trong repo này rồi push — **không cần đụng vào Make**.

## Sửa nội dung / ảnh

| Muốn đổi gì | Sửa file nào |
|---|---|
| Lời bài viết (caption) | `tools/gen_calendar.py` — biến `CAPS`, 16 chủ đề × 4 biến thể |
| Chữ & bố cục trên ảnh | `tools/gen_infographics.py` — biến `POSTS` |
| Màu ảnh | `tools/gen_infographics.py` — biến `THEMES` |
| Giờ mở cửa, Zalo, địa chỉ | 2 file trên (hằng số `GIO`, `Z`, `DC`, `HOURS`, `ADDR`) |
| Dùng ảnh chụp thật | bỏ ảnh vào `media/thuc-te/` (đọc file hướng dẫn trong đó) |

## Chạy lại sau khi sửa

```bash
python tools/gen_infographics.py media/auto      # sinh HTML 16 mẫu ảnh
python tools/render_png.py       media/auto      # chụp thành PNG 1080x1350
python tools/gen_calendar.py     media/auto media/lich   # rải ra 31 ngày x 2 buổi
python tools/build_posts_json.py                 # cập nhật posts.json
git add -A && git commit -m "Cap nhat noi dung" && git push
```

`render_png.py` cần Chrome/Chromium. Máy không tự tìm thấy thì chỉ đường:
`CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe" python tools/render_png.py media/auto`

## Quy tắc nội dung đang áp dụng

- Giờ mở cửa: **18h – 21h mỗi ngày** (ban ngày vẫn nhận Zalo đặt lịch).
- Bảo hành: **chỉ lỗi kỹ thuật / lỗi thi công** — bọt khí, bong tróc, hở mép, lệch viền.
  **Không** bảo hành trầy xước, va đập, hư hỏng do quá trình sử dụng.
- Không bịa giá, không bịa số liệu khách hàng.
