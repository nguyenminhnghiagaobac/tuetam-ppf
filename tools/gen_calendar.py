# -*- coding: utf-8 -*-
"""Ghep 16 anh + 64 caption thanh lich 31 ngay x 2 buoi = 62 bai.

Chay:  python tools/gen_calendar.py media/auto media/lich

Ket qua trong media/lich:
    ppf-dNN-08.png / .txt   -> bai dang luc 8h
    ppf-dNN-17.png / .txt   -> bai dang luc 17h
Scenario Make lay dung 2 file nay theo cong thuc ppf-d{DD}-{HH}.

Giong dieu: ban hang, bat mat, chot don. KHONG bia gia, khong bia so lieu.
Chinh sach bao hanh: CHI bao hanh loi ky thuat / loi thi cong
(bot khi, bong troc, ho mep, lech vien). KHONG bao hanh tray xuoc,
va dap, hu hong do qua trinh su dung.
"""
import os
import shutil
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "media/auto"
OUT = sys.argv[2] if len(sys.argv) > 2 else "media/lich"
os.makedirs(OUT, exist_ok=True)

WEB = "https://tuetamppf.vercel.app/"
Z = "📲 Zalo 0778.968.738"
GIO = "🕕 Mở cửa 18h – 21h mỗi ngày"
DC = "📍 71 đường số 2, khu CBGV, P. Tân An, TP Cần Thơ"
TAG = ("#TueTamPPF #PPFCanTho #DanPPFCanTho #CanTho #DanPPF "
       "#PPFDienThoai #PPFLaptop #PPFiPad")

CTA_MAC_DINH = "Nhắn Zalo tên máy — em báo giá liền, tư vấn miễn phí ạ!"


def bai(*doan, cta=CTA_MAC_DINH):
    """Ghep than bai + khoi chot don + hashtag."""
    than = "\n\n".join(d.strip() for d in doan if d.strip())
    return "%s\n\n👉 %s\n%s\n%s\n%s\n\n🌐 %s\n\n%s" % (than, cta, Z, GIO, DC, WEB, TAG)


CAPS = {
# ------------------------------------------------ 1. cuong luc khac PPF
1: [
bai("❌ SAI LẦM SỐ 1: nghĩ dán cường lực là máy an toàn rồi!",
    "Cường lực chỉ giữ đúng mặt kính trước thôi ạ.\n"
    "Lưng máy · viền máy · cụm camera — mấy chỗ trầy nhiều nhất mỗi ngày — "
    "thì cường lực không che tới một milimet nào.",
    "PPF là film trong suốt ôm trọn đúng mấy chỗ đó. Hai thứ này không thay nhau được đâu ạ."),
bai("Cường lực vỡ thì thay cái khác. Còn lưng máy trầy rồi thì… hết đường về 😢",
    "Đó là lý do PPF có mặt: nó lo phần thân máy mà cường lực bỏ trống — lưng, viền, cụm camera.",
    "Máy còn đẹp thì xài sướng, mà bán lại cũng được giá."),
bai("Máy anh chị đang trầy chỗ nào nhiều nhất? 🤔",
    "Em đoán không sai đâu: lưng máy và 4 góc viền.",
    "Đúng ngay mấy chỗ miếng cường lực không với tới. PPF sinh ra để lo phần đó — trong suốt, ôm sát, không làm dày máy."),
bai("Cường lực = cái nón bảo hiểm.\nPPF = bộ áo giáp cho cả thân máy.",
    "Hai thứ hoàn toàn khác nhau ạ. Dán đủ cả hai thì máy mới thật sự được bảo vệ.",
    "Ghé tiệm em coi máy mẫu trước khi quyết định cũng được nha."),
],
# ------------------------------------------------ 2. cat CNC
2: [
bai("Ở tiệm em, con dao KHÔNG bao giờ chạm vào máy của anh chị 🙅",
    "Film được máy CNC cắt sẵn theo đúng khuôn từng dòng máy rồi mới đem dán. "
    "Đặt lên là vừa khít — không hở viền, không lố qua cụm camera.",
    "Cắt tay ước chừng thì nhanh, nhưng lệch một chút là con mắt thấy liền."),
bai("Vì sao tên tiệm em có chữ CNC? 🎯",
    "Vì đó là thứ em tin nhất: máy cắt theo khuôn số của từng model, sai số cực nhỏ.",
    "Không đo bằng mắt. Không cắt bằng cảm giác. Không rọc dao trên máy khách."),
bai("Cùng gọi là dán PPF, nhưng khác nhau ở chỗ CẮT ✂️",
    "• Cắt tay: nhanh, rẻ, dễ lệch viền, dễ lố camera\n"
    "• Cắt CNC: đúng khuôn model, ôm sát từng đường bo",
    "Tiệm em chọn cách thứ hai, dù lâu hơn vài phút."),
bai("Máy anh chị đời nào cũng có khuôn cắt riêng 📐",
    "Kho khuôn CNC ở tiệm có sẵn rất nhiều dòng máy: điện thoại, máy tính bảng, laptop, đồng hồ.",
    "Nhắn tên máy qua Zalo, em kiểm tra có khuôn chưa rồi báo lại liền trong ngày.",
    cta="Nhắn tên máy qua Zalo, em check khuôn cắt giúp anh chị!"),
],
# ------------------------------------------------ 3. da thiet bi
3: [
bai("Không riêng điện thoại đâu ạ! 💯",
    "📱 Điện thoại · 📲 Máy tính bảng · 💻 Laptop · ⌚ Đồng hồ",
    "Máy nào cũng có khuôn cắt riêng. Anh chị đem một lần dán hết, khỏi chạy tới chạy lui nhiều chỗ."),
bai("Cả nhà mỗi người một máy? Gom một lượt cho gọn ạ 😊",
    "Điện thoại của ba mẹ, iPad của tụi nhỏ, laptop đi làm, đồng hồ thể thao — tiệm em nhận hết.",
    "Nhắn Zalo hẹn giờ trước, tối ghé là làm liền, khỏi ngồi chờ lâu."),
bai("Cái đồng hồ nhỏ xíu mà trầy mặt kính là thấy ngay 😔",
    "Mặt đồng hồ thông minh cũng dán PPF được ạ. Mỏng, trong, không ảnh hưởng cảm ứng, không cấn tay.",
    "Máy nào cũng có khuôn — cứ nhắn tên máy em kiểm tra."),
bai("MỘT CHỖ LO HẾT ✅",
    "Điện thoại, máy tính bảng, laptop, đồng hồ — cùng một tiêu chuẩn cắt CNC, cùng một cách làm kỹ.",
    "Đem tới, ngồi coi em dán tại chỗ, xong mang máy về luôn trong tối."),
],
# ------------------------------------------------ 4. laptop
4: [
bai("💻 Laptop mua mấy chục triệu mà nắp trầy nhem nhuốc thì tiếc lắm ạ!",
    "3 chỗ xuống cấp nhanh nhất: nắp lưng · chiếu nghỉ tay · viền màn hình.",
    "PPF phủ trong suốt, gõ phím vẫn êm, rê chuột vẫn mượt, mà nắp máy giữ được như mới."),
bai("Laptop bỏ balo mỗi ngày, cạ vô sách vở, khoá kéo, bàn quán cà phê… 😖",
    "Vài tháng là nắp máy đầy vệt xước nhỏ li ti — chùi cách gì cũng không hết.",
    "Dán PPF từ đầu là khỏi lo khoản đó."),
bai("Dân văn phòng và sinh viên chú ý nha 📌",
    "Chiếu nghỉ tay chỗ đặt cổ tay là nơi bong tróc, ố mòn sớm nhất trên laptop.",
    "Dán PPF phần đó vừa chống trầy vừa chống mồ hôi tay ăn vào máy."),
bai("Bán lại laptop, người mua soi cái nắp đầu tiên 👀",
    "Nắp còn nguyên → giữ giá. Nắp đầy vệt xước → bị trả giá xuống liền.",
    "Miếng film dán từ đầu rẻ hơn nhiều so với phần bị trừ giá đó ạ."),
],
# ------------------------------------------------ 5. may tinh bang
5: [
bai("📲 iPad / máy tính bảng: lưng nhôm trầy rồi là hết cứu!",
    "Để bàn ăn, đưa tụi nhỏ coi YouTube, bỏ chung balo với chìa khoá — trầy hồi nào không hay.",
    "Nhôm trầy thì đánh bóng cũng không về như cũ được đâu ạ."),
bai("Bao da KHÔNG cứu được lưng máy tính bảng đâu ạ ⚠️",
    "Bụi lọt vô giữa bao và lưng máy, mỗi lần đóng mở là mài một chút.",
    "Có lớp PPF ở dưới thì phần trầy đó film chịu, máy vẫn nguyên."),
bai("Màn to, lưng rộng — tablet trầy là thấy liền từ xa 😔",
    "Dán PPF lưng + viền một lần, xài mấy năm máy vẫn còn nét.",
    "Tiệm em có khuôn CNC cho nhiều dòng tablet, nhắn tên máy em check giúp."),
bai("Định bán tablet cũ lên đời máy mới? 📉",
    "Máy trầy là bị ép giá thẳng tay, khỏi thương lượng.",
    "Giữ lưng máy đẹp = giữ tiền trong túi mình ạ."),
],
# ------------------------------------------------ 6. mat gia khi ban lai
6: [
bai("💰 Người mua máy cũ lật LƯNG MÁY coi trước, chứ ít ai coi màn hình.",
    "Hai máy cùng đời, cùng dung lượng: cái lưng còn mới bán được giá, cái lưng đầy vết xước bị trả giá xuống.",
    "Miếng film dán từ đầu rẻ hơn rất nhiều so với phần bị mất giá."),
bai("Xước rồi là hết đường quay lại ạ ❌",
    "Đánh bóng, chà kem, dán decal che — cũng không về như máy zin được.",
    "Cách duy nhất là đừng để nó xước ngay từ đầu."),
bai("Máy mới mua về, nâng niu được đúng một tuần 😅",
    "Rồi để chung túi với chìa khoá, đặt xuống bàn đá, rớt nhẹ một cái… lưng máy bắt đầu có vết.",
    "Dán PPF sớm ngày nào lời ngày đó."),
bai("Anh chị định xài máy này bao lâu rồi đổi? 2 năm? 3 năm? ⏳",
    "Tới ngày bán lại, cái lưng máy quyết định anh chị được trả bao nhiêu.",
    "Đừng đợi trầy rồi mới đi dán — lúc đó film chỉ che chứ không xoá được vết cũ."),
],
# ------------------------------------------------ 7. bao hanh (quan trong)
7: [
bai("🛡️ CHÍNH SÁCH BẢO HÀNH — em nói rõ từ đầu cho anh chị dễ chọn:",
    "✅ CÓ bảo hành: nổi bọt khí, bong tróc, hở mép, lệch viền — nghĩa là mọi lỗi KỸ THUẬT do người dán gây ra. Mang ra em làm lại.",
    "❌ KHÔNG bảo hành: trầy xước trong quá trình sử dụng, va đập, rơi rớt, cấn móp, hoặc tự gỡ film ra dán lại.",
    "Nói thẳng vậy để anh chị yên tâm, không có chuyện hứa cho vui rồi tới lúc cần thì vòng vo ạ."),
bai("\"Dán PPF rồi film có bị trầy không em?\"",
    "Dạ CÓ chứ — và đó chính là việc của nó: film chịu trầy THAY cho máy. Trầy trên film thì thân máy bên dưới vẫn nguyên vẹn.",
    "Nên trầy do sử dụng thì em không bảo hành ạ. Còn nổi bọt khí, bong tróc, hở mép — lỗi thi công — thì em làm lại miễn phí."),
bai("Trước khi dán ở bất kỳ đâu, anh chị nhớ hỏi đúng 1 câu: BẢO HÀNH GỒM NHỮNG GÌ? 🔍",
    "Chỗ nào trả lời vòng vo, hứa \"bảo hành hết\" thì nên cân nhắc ạ — vì không ai bảo hành nổi vết trầy do người dùng làm ra.",
    "Tiệm em nói rõ: bảo hành lỗi kỹ thuật (bọt khí, bong tróc, hở mép). Không bảo hành trầy xước, va đập do sử dụng."),
bai("Phân biệt cho dễ nha anh chị 👇",
    "🔧 Lỗi của người dán: bọt khí, bong mép, hở viền, lệch khuôn → em chịu trách nhiệm, làm lại cho anh chị.",
    "👜 Do quá trình sử dụng: cạ chìa khoá, rớt, cấn góc, trầy mặt film → cái này film đã gánh thay máy rồi ạ, thay film mới là máy đẹp lại."),
],
# ------------------------------------------------ 8. gio mo cua moi
8: [
bai("📢 THÔNG BÁO GIỜ MỞ CỬA MỚI",
    "Tiệm em nhận khách tại chỗ từ 18h đến 21h mỗi ngày ạ 🕕",
    "Ban ngày em vẫn nhận tin nhắn Zalo: tư vấn, báo giá, đặt lịch bình thường. Tối ghé là dán liền, ngồi chờ lấy máy về luôn.",
    cta="Nhắn Zalo đặt lịch trước, tối ghé khỏi chờ!"),
bai("Tan làm → ăn cơm → chạy qua tiệm em, vẫn kịp nha 🌙",
    "Tiệm mở 18h – 21h mỗi ngày, kể cả cuối tuần.",
    "Nhắn Zalo trước một tiếng là em chuẩn bị sẵn film cho đúng máy anh chị, ghé tới làm liền.",
    cta="Nhắn Zalo hẹn giờ, tối ghé là có máy mang về!"),
bai("Ban ngày bận đi làm, không sắp xếp đi dán được? 😥",
    "Vậy thì hợp giờ tiệm em rồi: 18h – 21h mỗi tối.",
    "Anh chị cứ nhắn Zalo ban ngày để em báo giá và giữ chỗ, tối chạy qua là xong."),
bai("🕕 18h – 21h · MỖI NGÀY",
    "Đó là khung giờ em có mặt tại tiệm để dán cho anh chị.",
    "Ngoài giờ đó, tin nhắn Zalo em vẫn đọc và trả lời sớm nhất có thể ạ."),
],
# ------------------------------------------------ 9. dan au
9: [
bai("😤 Ham rẻ dán ẩu — vài ngày sau là biết liền!",
    "Hở viền · bọt khí li ti không tan · mép film cong lên bám bụi · lố qua cụm camera.",
    "Gỡ ra dán lại còn cực và tốn hơn lúc đầu. Dán một lần cho đúng vẫn hơn ạ."),
bai("4 dấu hiệu dán ẩu — anh chị tự kiểm tra máy mình được luôn 🔍",
    "1️⃣ Viền hở, lòi phần máy trần ra\n"
    "2️⃣ Bọt khí li ti nằm hoài không tan\n"
    "3️⃣ Mép film cong lên, đen sì vì bám bụi\n"
    "4️⃣ Film lố qua cụm camera, chụp bị mờ",
    "Máy đang bị mấy cái này thì mang ra em coi giúp cho ạ."),
bai("Xui nhất khi dán chỗ ẩu: bị rọc dao trúng khung máy 😱",
    "Vết dao đó ở lại vĩnh viễn, gỡ film ra vẫn còn.",
    "Tiệm em cắt CNC sẵn rồi mới dán — dao không bao giờ chạm vào máy khách."),
bai("Rẻ mà phải dán lại hai ba lần thì có còn rẻ không ạ? 🤔",
    "Em không dám nói tiệm em rẻ nhất. Em chỉ nói: làm cho đúng ngay từ lần đầu.",
    "Bọt khí, bong tróc do thi công — em làm lại miễn phí cho anh chị."),
],
# ------------------------------------------------ 10. khi nao nen dan
10: [
bai("⏰ 4 THỜI ĐIỂM NÊN DÁN PPF NGAY:",
    "1️⃣ Vừa bóc hộp máy mới — lúc máy còn nguyên vẹn nhất\n"
    "2️⃣ Vừa lỡ làm rơi một lần — lần sau chưa chắc còn hên\n"
    "3️⃣ Trước chuyến đi xa — máy va quẹt nhiều hơn ngày thường\n"
    "4️⃣ Máy mới chớm xước — đừng để vết đó lan thêm",
    "Trúng cái nào thì nhắn em nha ạ 😊"),
bai("✨ Máy mới bóc hộp là THỜI ĐIỂM VÀNG để dán.",
    "Lúc đó lưng máy chưa có một vết nào, dán vô là giữ nguyên trạng luôn.",
    "Để vài tuần rồi mới dán thì film chỉ che được vết cũ chứ không xoá được ạ."),
bai("Sắp đi du lịch hay đi công tác? Nhớ dán máy trước khi đi ✈️",
    "Đi chơi là lúc máy bị va quẹt nhiều nhất: nhét balo, để bãi biển, đưa người lạ chụp giùm.",
    "Dán trước một tối là yên tâm cả chuyến đi."),
bai("Mới mua máy cũ về xài? Dán PPF liền đi ạ 📱",
    "Để giữ nguyên tình trạng hiện tại, đừng cho nó xuống cấp thêm nữa.",
    "Em coi máy rồi tư vấn thật lòng nên dán phần nào cho đáng tiền."),
],
# ------------------------------------------------ 11. dep tu nhien
11: [
bai("\"Dán vô máy có bị dày, bị xấu không em?\" 🤔",
    "Dạ không ạ. Film PPF mỏng và trong suốt — dán rồi cầm lên cảm giác gần như máy trần.",
    "Không che logo, không làm máy phồng, không ám vàng. Ghé coi máy mẫu trước khi quyết định cũng được nha."),
bai("Máy đẹp thì phải khoe chứ giấu trong ốp nhựa dày cộm làm chi ạ 😄",
    "PPF trong suốt, giữ nguyên màu máy zin, nguyên đường bo, nguyên logo.",
    "Bảo vệ mà vẫn thấy được cái đẹp của máy."),
bai("Bỏ tiền mua máy mỏng đẹp rồi trùm ốp to đùng — hơi phí ạ 😅",
    "PPF mỏng dính, ôm sát thân máy, cầm vẫn đã tay mà vẫn chống trầy.",
    "Thích đeo thêm ốp cũng được, không bị kênh."),
bai("Film trong suốt nên màu máy zin sao thì thấy y vậy ✨",
    "Không đục, không ám vàng, không làm mất cảm giác vuốt chạm.",
    "Ghé tiệm coi tận mắt cho chắc rồi hãy dán nha anh chị."),
],
# ------------------------------------------------ 12. dia chi
12: [
bai("📍 TIỆM EM Ở ĐÂY NHA ANH CHỊ",
    "71 đường số 2, khu CBGV, P. Tân An, TP Cần Thơ.",
    "Dán PPF cho điện thoại, máy tính bảng, laptop, đồng hồ — cắt CNC chuẩn từng model.",
    "Mở cửa 18h – 21h mỗi ngày, nhắn Zalo trước cho khỏi chờ ạ."),
bai("Anh chị ở Cần Thơ hoặc mấy huyện lân cận cần dán PPF thì ghé em nha 🤍",
    "71 đường số 2, khu CBGV, P. Tân An — chạy tới đầu đường số 2 là thấy bảng hiệu TUỆ TÂM.",
    "Không biết đường thì nhắn Zalo, em chỉ đường cho khỏi lạc 😊"),
bai("Tìm số 71, đường số 2, khu CBGV, phường Tân An 🏠",
    "Bảng hiệu TUỆ TÂM – PPF CNC CẦN THƠ, mở đèn từ 18h tối.",
    "Anh chị ghé là có người tiếp liền, không phải chờ."),
bai("Ghé tiệm không cần hẹn cũng được ạ 😊",
    "Nhưng nhắn Zalo trước thì em chuẩn bị sẵn film đúng dòng máy, anh chị tới là dán liền, đỡ ngồi chờ.",
    "Tiệm mở 18h – 21h mỗi ngày, kể cả cuối tuần."),
],
# ------------------------------------------------ 13. op lung vs PPF
13: [
bai("Ốp lưng CHE máy. PPF CỨU máy. Khác nhau đó ạ 😊",
    "Ốp dày cộm, làm nóng máy, mất dáng đẹp. PPF mỏng dính mà vẫn chống trầy 24/7.",
    "Thích thì dán PPF rồi đeo ốp chồng lên cũng được, không bị kênh."),
bai("\"Đeo ốp rồi có cần PPF nữa không em?\"",
    "Dạ cần ạ. Vì lúc tháo ốp ra lau máy, cắm sạc, đưa người khác coi — mấy lúc đó máy trần hoàn toàn.",
    "Và đó cũng là mấy lúc máy hay bị trầy nhất."),
bai("Ốp silicon xài lâu bị ố vàng — mà bụi lọt vô trong ốp còn mài xước lưng máy nữa 😖",
    "Nhiều anh chị tháo ốp ra mới hoảng: lưng máy xước mờ hết một mảng.",
    "Có PPF ở dưới thì phần trầy đó film chịu, máy vẫn đẹp nguyên."),
bai("PPF hay ốp lưng? Em trả lời thật lòng: CẢ HAI 🤝",
    "PPF chống trầy hằng ngày, ốp giảm sốc khi rơi — mỗi cái một việc.",
    "Ai thích cầm máy trần cho đã tay thì PPF là bắt buộc."),
],
# ------------------------------------------------ 14. camera & vien
14: [
bai("📸 Anh chị để ý mà coi: đặt máy xuống bàn là CỤM CAMERA chạm mặt bàn trước tiên.",
    "Đó là chỗ trầy sớm nhất, mà cũng là chỗ ảnh hưởng chất lượng chụp hình nhiều nhất.",
    "PPF che được đúng chỗ đó — cường lực thì không."),
bai("Camera trầy = hình bị mờ, bị loá khi chụp ngược sáng 😔",
    "Sửa thì tốn, thay cụm camera còn tốn hơn nhiều lần miếng film.",
    "Dán che cụm camera ngay từ đầu là rẻ nhất ạ."),
bai("Rớt nhẹ một cái là 4 góc viền ăn đủ 💥",
    "Chỗ đó cường lực không che, ốp thì hay hở, mà lại là chỗ va chạm nhiều nhất.",
    "PPF ôm sát viền, đỡ được mấy vết va quẹt hằng ngày."),
bai("Lật máy lên coi cụm camera thử đi ạ 👀",
    "Có vết xước nhỏ nào chưa? Nếu có rồi thì nên dán ngay để nó đừng lan thêm.",
    "Chưa có vết nào thì càng nên dán — giữ nguyên vậy luôn."),
],
# ------------------------------------------------ 15. chon tiem
15: [
bai("🔍 TRƯỚC KHI GIAO MÁY, HỎI 3 CÂU NÀY LÀ BIẾT TIỆM CÓ NGON KHÔNG:",
    "1️⃣ Có cắt bằng máy CNC theo đúng model máy em không?\n"
    "2️⃣ Có rọc dao trực tiếp lên máy khách không?\n"
    "3️⃣ Bảo hành ra sao nếu film nổi bọt, bong tróc?",
    "Chỗ nào trả lời rõ ràng, dứt khoát thì anh chị yên tâm giao máy ạ."),
bai("Tiệm nào cho anh chị coi khuôn cắt đúng dòng máy mình TRƯỚC khi dán — đó là dấu hiệu tốt 👍",
    "Vì có khuôn sẵn nghĩa là họ làm đúng model, không cắt ước chừng.",
    "Nhắn tên máy qua Zalo, em kiểm tra khuôn rồi báo lại cho anh chị coi."),
bai("Chọn chỗ dán PPF cũng như chọn thợ cắt tóc vậy 😅",
    "Làm ẩu một lần là nhớ đời, mà máy thì không mọc lại như tóc được.",
    "Hỏi kỹ, coi kỹ, rồi hãy giao máy ạ."),
bai("Em không sợ anh chị đi so sánh nhiều nơi 🤍",
    "Em chỉ sợ anh chị dán nhầm chỗ ẩu rồi mất niềm tin với PPF luôn.",
    "Cứ hỏi kỹ bảo hành và cách cắt film trước khi giao máy, ở đâu cũng vậy."),
],
# ------------------------------------------------ 16. chot don
16: [
bai("⚡ NHẮN TÊN MÁY — EM BÁO GIÁ LIỀN",
    "Anh chị chỉ cần nhắn Zalo: tên máy + muốn dán phần nào (lưng, viền, camera, màn hình).",
    "Em kiểm tra khuôn cắt, báo giá rõ ràng, tư vấn thật lòng. Không dán cũng không sao ạ 😊"),
bai("Chưa biết máy mình dán được kiểu nào cho đáng tiền? 🤔",
    "Nhắn tên máy qua Zalo, em coi rồi tư vấn: máy này nên dán full thân hay chỉ lưng + camera là đủ.",
    "Tư vấn miễn phí, em không ép anh chị dán đâu."),
bai("TUỆ TÂM PPF CNC CẦN THƠ 🤍",
    "• Cắt CNC chuẩn từng dòng máy, không rọc dao lên máy khách\n"
    "• Nhận điện thoại, máy tính bảng, laptop, đồng hồ\n"
    "• Bảo hành lỗi kỹ thuật: bọt khí, bong tróc, hở mép\n"
    "• Dán tại chỗ, ngồi chờ lấy máy về trong tối",
    "Mở cửa 18h – 21h mỗi ngày."),
bai("Bảo vệ máy không phải chuyện xa xỉ — là chuyện giữ tiền của mình ạ 💰",
    "Một miếng film dán từ đầu, đổi lại cái máy còn đẹp suốt mấy năm và bán lại không bị ép giá.",
    "Nhắn em một tiếng, em tính giúp cho anh chị coi có đáng không."),
],
}

SO_CHU_DE = len(CAPS)
SO_BIEN_THE = min(len(v) for v in CAPS.values())


def main():
    made = 0
    for day in range(1, 32):
        for si, gio in enumerate(("08", "17")):
            idx = (day - 1) * 2 + si                    # 0..61
            chu_de = idx % SO_CHU_DE + 1                # xoay vong chu de
            bien_the = (idx // SO_CHU_DE) % SO_BIEN_THE  # doi loi van moi vong
            nguon_anh = os.path.join(SRC, "ppf-%02d.png" % chu_de)
            ten = "ppf-d%02d-%s" % (day, gio)
            shutil.copyfile(nguon_anh, os.path.join(OUT, ten + ".png"))
            with open(os.path.join(OUT, ten + ".txt"), "w", encoding="utf-8") as f:
                f.write(CAPS[chu_de][bien_the])
            made += 1
    print("Da tao %d bai (anh + caption) tu %d chu de x %d bien the"
          % (made, SO_CHU_DE, SO_BIEN_THE))


if __name__ == "__main__":
    main()
