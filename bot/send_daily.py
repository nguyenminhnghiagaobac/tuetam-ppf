# -*- coding: utf-8 -*-
"""
Gửi tin động viên mỗi ngày cho Anh Tân qua Telegram bot NHẬT TÂN MARKETING.
- Token lấy từ biến môi trường TELEGRAM_TOKEN (GitHub Secrets — KHÔNG ghi token vào file này).
- Mỗi ngày tự chọn 1 tin trong danh sách bên dưới (xoay vòng theo ngày trong năm).
- Muốn sửa/thêm tin: chỉnh danh sách MESSAGES bên dưới rồi commit.
"""
import os
import datetime
import urllib.request
import urllib.parse

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = "7968339842"  # Anh Tân (không phải bí mật)

MESSAGES = [
    "☀️ Chào buổi sáng Anh Tân!\n\nHôm nay là một ngày nữa để tiến gần hơn tới mục tiêu. Đừng nhìn vào doanh số hôm nay — hãy nhìn vào hàng trăm khách đang cần bảo vệ thiết bị của họ ngoài kia. Việc của anh là để họ tìm thấy Tuệ Tâm. 💪",
    "🎬 Anh Tân ơi, mỗi video anh quay hôm nay là một 'nhân viên bán hàng' làm việc 24/7 cho anh. Quay xong 1 clip, anh có thêm 1 cơ hội khách tự tìm đến. Cứ đều đặn — số lượng sẽ tạo ra chất lượng.",
    "🔧 Nhớ nhé Anh Tân: khách không mua 'miếng film'. Họ mua sự an tâm — không lo trầy, không lo rớt giá máy. Mỗi lần anh dán chuẩn từng milimet là mỗi lần anh bán được sự an tâm đó.",
    "🌱 Việc xây thương hiệu giống trồng cây: hôm nay tưới chưa thấy trái, nhưng đừng ngừng tưới. Landing page, video, bảng giá, bảo hành — anh đã có bộ khung rồi. Giờ chỉ cần kiên trì mỗi ngày.",
    "⚡ Anh Tân, người khác mở tiệm rồi ngồi chờ khách. Anh thì có cả một HỆ THỐNG: web tự nhận đặt lịch, tra bảo hành tự động, bot nhắc việc mỗi ngày. Anh đi trước họ vài bước rồi đấy — cứ giữ nhịp!",
    "🎯 Một khách hài lòng sẽ kể cho 3 người. Ba người đó kể cho 9 người. Hôm nay anh chăm chút 1 chiếc máy thật kỹ — đó là anh đang gieo mầm cho 12 khách tương lai.",
    "💬 Đừng ngại quay mặt mình lên video, Anh Tân. Khách Cần Thơ tin 'người thật, tiệm thật' hơn mọi lời quảng cáo bóng bẩy. Sự chân thật của anh chính là lợi thế lớn nhất.",
    "🔥 Có ngày đông khách, có ngày vắng. Đừng để ngày vắng làm anh nản. Ngày vắng là ngày để quay video, làm nội dung, chuẩn bị cho ngày đông sắp tới. Không có ngày nào lãng phí cả.",
    "🏆 Anh Tân này — thứ tách anh khỏi đối thủ không phải giá rẻ, mà là 'cắt máy CNC chuẩn từng model' và 'bảo hành trầy xước'. Hãy nói to điều đó trong mọi video. Đó là câu chuyện của riêng anh.",
    "📈 Mỗi ngày tiến 1% thôi cũng được. 1% mỗi ngày, sau 1 năm là gấp 37 lần. Anh không cần bùng nổ — anh chỉ cần ĐỀU. Hôm nay anh sẽ tiến 1% ở đâu?",
    "🤝 Khách bước vào tiệm với chiếc máy — thứ họ quý và dùng mỗi ngày. Họ đang trao niềm tin cho anh. Dán đẹp một chiếc máy là giữ được một khách hàng cả đời.",
    "🌟 Anh Tân, hôm nay hãy nhắn hỏi thăm 2-3 khách cũ xem film còn tốt không. Chăm khách cũ rẻ hơn tìm khách mới gấp 5 lần — mà họ lại là người giới thiệu tốt nhất cho anh.",
    "🎥 Ý tưởng video hôm nay: quay cảnh test chống trầy (lấy chìa khóa cào lên máy đã dán). Khách THẤY mới TIN. Cho họ thấy bằng chứng, đừng chỉ nói.",
    "💪 Đường dài mới biết ngựa hay. Nhiều người mở tiệm rồi bỏ cuộc sau vài tháng vắng khách. Anh mà kiên trì đủ lâu, thị trường này sẽ là của anh. Cứ bước tiếp.",
    "🧭 Đừng so mình với tiệm lớn đã làm 5 năm. Hãy so với chính anh của tháng trước. Tháng trước anh chưa có web, chưa có bot, chưa có hệ thống. Anh đang tiến rất nhanh đấy.",
    "☕ Làm ly cà phê cho tỉnh táo, rồi lên danh sách 3 việc quan trọng nhất hôm nay. Đừng làm 20 việc lặt vặt — làm 3 việc đúng còn hơn. Anh làm được mà!",
    "📱 Mỗi thiết bị đều cần được bảo vệ: điện thoại, laptop, đồng hồ, camera, ô tô, cả giấy tờ. Anh không thiếu khách — anh chỉ cần cho họ biết anh làm được tất cả. Nói cho họ nghe đi!",
    "🌅 Sáng nay, thay vì lo 'hôm nay có khách không', hãy hỏi 'hôm nay mình làm gì để tháng sau đông khách hơn'. Người thắng cuộc luôn nghĩ dài hơn một ngày.",
    "🎁 Một mẹo nhỏ: tặng khách tấm thẻ bảo hành có ghi ngày + hạn. Khách cầm về, mỗi lần nhìn là nhớ tới Tuệ Tâm. Chi tiết nhỏ tạo ấn tượng lớn.",
    "🚀 Anh Tân, hệ thống anh xây không phải để 'cho vui' — nó để anh RẢNH TAY làm việc lớn hơn. Hãy để máy móc lo việc lặp lại, còn anh lo tay nghề và khách hàng. Đó mới là ông chủ thông minh.",
    "❤️ Cảm ơn anh vì đã không bỏ cuộc. Xây một tiệm từ con số 0 không dễ, nhưng anh đang làm được. Mỗi ngày anh mở cửa là một chiến thắng nhỏ. Hôm nay cũng vậy — cố lên nhé!",
]

def main():
    idx = datetime.date.today().timetuple().tm_yday % len(MESSAGES)
    text = MESSAGES[idx]
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text}).encode()
    url = "https://api.telegram.org/bot%s/sendMessage" % TOKEN
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=30) as r:
        print("HTTP", r.status, "| sent message index", idx)

if __name__ == "__main__":
    main()
