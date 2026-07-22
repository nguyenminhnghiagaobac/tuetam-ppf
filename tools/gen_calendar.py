# -*- coding: utf-8 -*-
"""Ghep 14 anh + caption thanh lich 31 ngay x 2 buoi (sang/chieu) = 62 bai."""
import os, sys, shutil

SRC = sys.argv[1]   # thu muc chua ppf-01..14.png
OUT = sys.argv[2]   # thu muc dich trong repo
os.makedirs(OUT, exist_ok=True)

Z = "Zalo 0778.968.738"
TAG = "#TueTamPPF #PPFCanTho #CanTho #DanPPF"
DC = "71 đường số 2, khu CBGV, P. Tân An, TP Cần Thơ · Mở 8h-21h"

# 14 chu de, moi chu de 5 caption khac nhau -> 70 caption cho 62 o
CAPS = {
1: [  # cuong luc vs PPF
"Nhiều anh chị hỏi em: dán cường lực rồi thì cần chi PPF nữa?\n\nDạ hai cái lo hai chỗ khác nhau ạ. Cường lực giữ mặt kính trước. Còn lưng máy, viền máy, cụm camera — mấy chỗ trầy nhiều nhất mỗi lần để bàn hay bỏ túi chung chìa khoá — thì cường lực không che tới.\n\nPPF là film trong suốt ôm trọn mấy chỗ đó.\n\nAnh chị nhắn " + Z + " em tư vấn miễn phí nha 🤍\n\n" + TAG,
"Cường lực vỡ thì thay cái mới. Lưng máy trầy thì… chịu 😢\n\nĐó là lý do PPF ra đời. Nó ôm phần thân máy mà cường lực bỏ sót: lưng, viền, cụm camera.\n\nHai thứ này không thay thế nhau, dùng chung mới đủ.\n\nNhắn " + Z + " em tư vấn cho máy của anh chị nha.\n\n" + TAG,
"Câu hỏi em nghe mỗi ngày: PPF với cường lực cái nào tốt hơn?\n\nDạ không so được, vì mỗi cái lo một phần máy khác nhau ạ.\n\nCường lực → mặt kính trước\nPPF → lưng, viền, camera\n\nMuốn máy nguyên vẹn thì cần cả hai.\n\n" + Z + "\n\n" + TAG,
"Máy anh chị đang trầy chỗ nào nhiều nhất? Em đoán là lưng máy với 4 góc viền đúng không ạ 😊\n\nĐúng mấy chỗ mà miếng cường lực không với tới. PPF sinh ra để lo phần đó.\n\nGhé tiệm em coi thử, không dán cũng không sao.\n\n" + Z + "\n\n" + TAG,
"Dán cường lực = mua nón bảo hiểm.\nDán PPF = mặc áo giáp cho cả người.\n\nHai thứ khác nhau hoàn toàn ạ 😄\n\nAnh chị cần tư vấn cứ nhắn " + Z + " nha.\n\n" + TAG],
2: [  # CNC
"Tiệm em không rọc dao trực tiếp lên máy khách 🙅\n\nFilm được cắt sẵn bằng máy CNC theo đúng khuôn từng dòng máy. Đặt lên là vừa khít, không hở viền, không lố mép.\n\nCắt tay ước chừng thì nhanh, nhưng lệch một chút là thấy liền.\n\n" + Z + "\n\n" + TAG,
"Vì sao tiệm em tên là TUỆ TÂM PPF CNC?\n\nVì CNC là thứ em tin nhất: máy cắt theo khuôn số của từng model, sai số cực nhỏ. Máy anh chị đời nào cũng có khuôn riêng.\n\nKhông đo bằng mắt, không cắt bằng cảm giác.\n\n" + Z + "\n\n" + TAG,
"Cùng là dán PPF, khác nhau ở chỗ cắt.\n\nCắt tay: nhanh, rẻ, dễ lệch viền, dễ lố qua cụm camera.\nCắt CNC: đúng khuôn model, ôm sát, gọn gàng.\n\nTiệm em chọn cách thứ hai.\n\n" + Z + "\n\n" + TAG,
"Có anh mang máy tới, kể chỗ cũ rọc dao ngay trên lưng máy, xong để lại vết trên khung 😖\n\nỞ tiệm em không có chuyện đó. Film cắt sẵn bằng CNC rồi mới đem dán.\n\nDao không bao giờ chạm vào máy anh chị.\n\n" + Z + "\n\n" + TAG,
"Máy cắt CNC ở tiệm có sẵn khuôn cho rất nhiều dòng máy.\n\nAnh chị nhắn tên máy qua Zalo, em kiểm tra có khuôn chưa rồi báo lại liền.\n\n" + Z + "\n\n" + TAG],
3: [  # da thiet bi
"Không riêng điện thoại đâu ạ 😊\n\nĐiện thoại · Máy tính bảng · Laptop · Đồng hồ\n\nMáy nào cũng có khuôn cắt riêng. Anh chị đem một lần dán hết, khỏi chạy nhiều chỗ.\n\n" + Z + "\n\n" + TAG,
"Laptop mới mua mà để trần thì tiếc lắm ạ. Nắp lưng với chiếu nghỉ tay là hai chỗ xuống cấp nhanh nhất.\n\nTiệm em dán PPF cho laptop, tablet, đồng hồ chứ không riêng điện thoại.\n\n" + Z + "\n\n" + TAG,
"Cả nhà mỗi người một máy? Đem hết ra một lượt cho tiện ạ.\n\nĐiện thoại, tablet, laptop, đồng hồ — tiệm em nhận hết, mỗi loại một khuôn riêng.\n\nNhắn " + Z + " hẹn giờ trước cho khỏi chờ nha.\n\n" + TAG,
"Cái đồng hồ thông minh nhỏ xíu mà trầy mặt kính là thấy ngay 😔\n\nMặt đồng hồ cũng dán PPF được ạ. Mỏng, trong, không ảnh hưởng cảm ứng.\n\n" + Z + "\n\n" + TAG,
"Một chỗ lo hết: điện thoại, tablet, laptop, đồng hồ.\n\nCùng một tiêu chuẩn cắt CNC, cùng một cách làm.\n\nGhé tiệm em ở " + DC + "\n\n" + TAG],
4: [  # mat gia
"Chuyện thật: hai cái máy cùng đời, cùng dung lượng.\n\nCái giữ kỹ, lưng còn mới → bán được giá.\nCái lưng đầy vết xước → bị trả giá xuống.\n\nMiếng film dán từ đầu rẻ hơn nhiều so với phần bị mất giá đó ạ.\n\n" + Z + "\n\n" + TAG,
"Anh chị định xài máy này bao lâu rồi đổi? 2 năm? 3 năm?\n\nTới lúc bán lại, người mua sẽ lật lưng máy ra coi đầu tiên. Trầy nhiều là bị ép giá liền.\n\nGiữ lưng máy đẹp = giữ tiền cho mình.\n\n" + Z + "\n\n" + TAG,
"Xước rồi là hết đường quay lại ạ. Đánh bóng cũng không về như cũ được.\n\nCách duy nhất là đừng để nó xước ngay từ đầu.\n\n" + Z + "\n\n" + TAG,
"Máy mới mua về, nâng niu được đúng một tuần 😅\n\nRồi để chung túi với chìa khoá, đặt xuống bàn đá, rớt nhẹ một cái... lưng máy bắt đầu có vết.\n\nDán PPF từ đầu là yên tâm luôn.\n\n" + Z + "\n\n" + TAG,
"Đừng đợi máy trầy rồi mới đi dán ạ. Lúc đó film chỉ che được vết cũ chứ không xoá được.\n\nDán sớm ngày nào lời ngày đó.\n\n" + Z + "\n\n" + TAG],
5: [  # bao hanh
"Dán xong mà lỡ trầy film thì sao ạ?\n\nDạ tiệm em có bảo hành trầy xước. Trong thời gian bảo hành, anh chị cứ mang máy ra em xử lý.\n\nNói rõ ràng từ đầu để anh chị yên tâm 🤍\n\n" + Z + "\n\n" + TAG,
"Em không hứa film không bao giờ trầy — nói vậy là xạo ạ.\n\nEm hứa cái khác: trầy thì có bảo hành, mang ra tiệm em lo.\n\nCam kết được cái gì thì nói cái đó.\n\n" + Z + "\n\n" + TAG,
"Trước khi dán ở bất kỳ đâu, anh chị nhớ hỏi kỹ: bảo hành thế nào, bao lâu, gồm những gì?\n\nChỗ nào nói vòng vo là nên cân nhắc ạ.\n\nTiệm em nói rõ ngay từ đầu.\n\n" + Z + "\n\n" + TAG,
"Có bảo hành trầy xước nên anh chị cứ dùng máy thoải mái.\n\nBỏ túi chung chìa khoá, để bàn, đưa con nít cầm — có gì mang ra em.\n\n" + Z + "\n\n" + TAG,
"Dán PPF ở tiệm em xong, anh chị giữ lại thông tin để tra bảo hành nha.\n\nCần gì cứ nhắn " + Z + " em kiểm tra giúp.\n\n" + TAG],
6: [  # gio mo cua
"Tiệm em mở 8h sáng tới 9h tối mỗi ngày ạ ☀️🌙\n\nAnh chị đi làm về ghé vẫn kịp. Nhắn Zalo trước một tiếng thì em chuẩn bị sẵn, khỏi ngồi chờ lâu.\n\n" + Z + "\n" + DC + "\n\n" + TAG,
"Chiều tan làm ghé tiệm em nha anh chị 😊\n\nMở tới 9h tối, không nghỉ trưa.\n\n" + DC + "\n\n" + TAG,
"Cuối tuần rảnh thì đem máy ra tiệm em nha. 8h sáng tới 9h tối, ngày nào cũng mở.\n\nNhắn " + Z + " trước cho chắc ăn.\n\n" + TAG,
"Sáng ghé, chiều ghé, tối ghé — giờ nào tiệm em cũng có người ạ. 8h - 21h.\n\n" + DC + "\n\n" + TAG,
"Bận quá không sắp xếp được giờ? Nhắn " + Z + " em hẹn khung giờ tiện cho anh chị nha.\n\nTiệm mở 8h-21h mỗi ngày.\n\n" + TAG],
7: [  # cho khong uy tin
"Film chợ, cắt tay, dán vội — vài ngày sau là biết ạ 😖\n\nHở viền. Bong mép. Nổi bọt khí. Gỡ ra dán lại còn mệt hơn lúc đầu.\n\nDán một lần cho đúng vẫn hơn ạ.\n\n" + Z + "\n\n" + TAG,
"Dấu hiệu dán ẩu anh chị tự kiểm tra được:\n\n• Viền hở, thấy phần máy trần lòi ra\n• Có bọt khí li ti không tan\n• Mép film cong lên, bám bụi\n• Lố qua cụm camera\n\nGặp mấy cái này là nên đi làm lại ạ.\n\n" + Z + "\n\n" + TAG,
"Rẻ mà dán lại hai ba lần thì có còn rẻ không ạ? 🤔\n\nEm không nói tiệm em rẻ nhất. Em nói làm cho đúng ngay lần đầu.\n\n" + Z + "\n\n" + TAG,
"Bọt khí dưới film không tự hết đâu ạ. Nó là do dán không đúng cách chứ không phải chờ vài ngày là tan.\n\nMáy anh chị đang bị vậy thì mang ra em coi giúp.\n\n" + Z + "\n\n" + TAG,
"Ham rẻ dán chỗ ẩu, xui nhất là bị rọc dao trúng khung máy. Vết đó ở lại vĩnh viễn 😔\n\nTiệm em cắt CNC sẵn, dao không chạm máy.\n\n" + Z + "\n\n" + TAG],
8: [  # khi nao nen dan
"4 lúc nên dán PPF ngay:\n\n1. Vừa mua máy mới — lúc máy còn nguyên vẹn nhất\n2. Vừa lỡ làm rơi một lần — lần sau chưa chắc may vậy\n3. Trước chuyến đi xa — máy va chạm nhiều hơn ngày thường\n4. Máy bắt đầu có vết xước nhỏ — đừng để nó lan\n\n" + Z + "\n\n" + TAG,
"Máy mới bóc hộp là thời điểm vàng để dán ạ ✨\n\nLúc đó lưng máy chưa có một vết nào. Dán vô là giữ được nguyên trạng luôn.\n\n" + Z + "\n\n" + TAG,
"Sắp đi du lịch hay đi công tác? Nhớ dán máy trước khi đi ạ.\n\nĐi chơi là lúc máy bị va quẹt nhiều nhất: bỏ balo, để bãi biển, đưa người khác chụp giùm.\n\n" + Z + "\n\n" + TAG,
"Vừa làm rơi máy mà máy còn nguyên? Hên đó ạ 😅\n\nLần sau chưa chắc hên vậy. Tranh thủ dán đi anh chị.\n\n" + Z + "\n\n" + TAG,
"Mua máy cũ về xài? Dán PPF luôn đi ạ, để giữ nguyên tình trạng hiện tại, đừng cho nó xuống cấp thêm.\n\n" + Z + "\n\n" + TAG],
9: [  # dep tu nhien
"Nhiều anh chị sợ dán vô máy bị dày, bị xấu.\n\nDạ film PPF mỏng và trong ạ. Dán rồi cầm lên cảm giác gần như máy trần, không che logo, không làm máy phồng lên.\n\nGhé tiệm em coi máy mẫu trước khi quyết định nha.\n\n" + Z + "\n\n" + TAG,
"Máy đẹp thì phải khoe chứ giấu trong ốp làm gì ạ 😄\n\nPPF trong suốt, giữ nguyên màu máy, nguyên logo. Bảo vệ mà vẫn thấy máy.\n\n" + Z + "\n\n" + TAG,
"Bỏ tiền mua máy đẹp rồi trùm ốp nhựa dày cộm — hơi phí ạ 😅\n\nPPF mỏng dính, giữ nguyên dáng máy, mà vẫn chống trầy.\n\n" + Z + "\n\n" + TAG,
"Dán PPF rồi vẫn đeo ốp bình thường được ạ, không bị kênh.\n\nAnh chị thích cầm trần thì càng hợp.\n\n" + Z + "\n\n" + TAG,
"Film trong suốt nên màu máy zin thế nào thì thấy y vậy. Không ám vàng, không đục.\n\nGhé coi tận mắt cho chắc nha anh chị.\n\n" + DC + "\n\n" + TAG],
10: [ # dia chi
"📍 Tiệm em ở đây nha anh chị:\n\n" + DC + "\n" + Z + "\n\nDán PPF cho điện thoại, tablet, laptop, đồng hồ. Cắt CNC chuẩn từng model.\n\n" + TAG,
"Anh chị ở Cần Thơ hoặc các huyện lân cận, cần dán PPF thì ghé em nha.\n\n" + DC + "\n" + Z + "\n\n" + TAG,
"Đường số 2, khu CBGV, phường Tân An — anh chị tìm số 71 nha.\n\nNhắn " + Z + " em chỉ đường cho, khỏi lạc 😊\n\n" + TAG,
"Ghé tiệm không cần hẹn cũng được ạ, nhưng nhắn Zalo trước thì em chuẩn bị sẵn film, anh chị đỡ chờ.\n\n" + DC + "\n" + Z + "\n\n" + TAG,
"TUỆ TÂM PPF CNC CẦN THƠ\n" + DC + "\n" + Z + "\n\nMở cửa mỗi ngày, ghé em bất cứ lúc nào ạ 🤍\n\n" + TAG],
11: [ # op lung
"Ốp lưng che máy. PPF cứu máy. Khác nhau đó ạ 😊\n\nỐp dày cộm, làm máy nóng, mất dáng đẹp. PPF mỏng dính mà vẫn chống trầy.\n\nThích thì dán PPF rồi đeo ốp luôn cũng được.\n\n" + Z + "\n\n" + TAG,
"Đeo ốp rồi có cần PPF nữa không ạ?\n\nDạ cần, vì lúc anh chị tháo ốp ra lau máy, cắm sạc, hay đưa người khác coi — mấy lúc đó máy trần hoàn toàn.\n\n" + Z + "\n\n" + TAG,
"Ốp silicon xài lâu bị ố vàng, mà bụi lọt vô trong ốp còn mài xước lưng máy nữa ạ 😖\n\nCó PPF ở dưới thì phần trầy đó film chịu, máy không sao.\n\n" + Z + "\n\n" + TAG,
"Máy mỏng đẹp mà đeo ốp dày thì uổng lắm ạ. Dán PPF là giải pháp cho ai thích cầm máy trần.\n\n" + Z + "\n\n" + TAG,
"PPF hay ốp lưng? Câu trả lời thật lòng: cả hai, mỗi cái một việc.\n\nPPF chống trầy hằng ngày. Ốp giảm sốc khi rơi.\n\n" + Z + "\n\n" + TAG],
12: [ # camera & vien
"Anh chị để ý mà coi: đặt máy xuống bàn là cụm camera chạm mặt bàn trước tiên 📸\n\nĐó là chỗ trầy sớm nhất, mà cũng là chỗ ảnh hưởng chất lượng chụp hình nhất.\n\nPPF che được chỗ đó.\n\n" + Z + "\n\n" + TAG,
"Rớt nhẹ một cái là 4 góc viền ăn đủ. Chỗ đó cường lực không che, ốp thì hay hở.\n\nPPF ôm sát viền, đỡ được mấy vết va quẹt hằng ngày.\n\n" + Z + "\n\n" + TAG,
"Camera trầy là hình bị mờ, bị loá khi chụp ngược sáng. Sửa thì tốn, mà thay cụm camera còn tốn hơn.\n\nDán film che cụm camera từ đầu rẻ hơn nhiều ạ.\n\n" + Z + "\n\n" + TAG,
"Hai chỗ khách hay tiếc nhất khi trầy: cụm camera và 4 góc viền.\n\nHai chỗ đó tiệm em dán kỹ nhất.\n\n" + Z + "\n\n" + TAG,
"Máy anh chị lật lên coi cụm camera thử ạ. Có vết xước nhỏ nào chưa?\n\nNếu có rồi thì nên dán ngay để nó đừng lan thêm.\n\n" + Z + "\n\n" + TAG],
13: [ # checklist chon tiem
"Trước khi dán ở đâu, anh chị hỏi 3 câu này là biết chỗ đó có ngon không:\n\n1. Có cắt bằng máy CNC theo model không, hay cắt tay?\n2. Có rọc dao trực tiếp lên máy em không?\n3. Bảo hành ra sao nếu film bong hay trầy?\n\nChỗ nào trả lời rõ ràng thì yên tâm ạ.\n\n" + Z + "\n\n" + TAG,
"Em không sợ anh chị so sánh, em chỉ sợ anh chị dán nhầm chỗ rồi mất niềm tin với PPF luôn 😔\n\nCứ hỏi kỹ trước khi dán, ở đâu cũng vậy.\n\n" + Z + "\n\n" + TAG,
"Đi dán PPF nhớ hỏi kỹ về bảo hành nha anh chị. Đây là thứ phân biệt tiệm làm ăn lâu dài với chỗ làm cho xong.\n\n" + Z + "\n\n" + TAG,
"Tiệm nào cho anh chị coi khuôn cắt của đúng dòng máy mình trước khi dán thì đó là dấu hiệu tốt ạ 👍\n\n" + Z + "\n\n" + TAG,
"Chọn chỗ dán PPF cũng như chọn thợ cắt tóc vậy — làm ẩu một lần là nhớ đời 😅\n\nHỏi kỹ, coi kỹ, rồi hãy giao máy.\n\n" + Z + "\n\n" + TAG],
14: [ # tong hop
"TUỆ TÂM PPF CNC CẦN THƠ 🤍\n\n• Cắt CNC chuẩn từng dòng máy\n• Điện thoại, tablet, laptop, đồng hồ\n• Không rọc dao lên máy khách\n• Có bảo hành trầy xước\n\n" + DC + "\n" + Z + "\n\n" + TAG,
"Dán một lần, yên tâm dài lâu ạ.\n\nMáy cắt CNC chuẩn model, film ôm khít viền, có bảo hành trầy xước.\n\nNhắn " + Z + " để em tư vấn cho đúng máy của anh chị.\n\n" + TAG,
"Cảm ơn anh chị đã tin tiệm em thời gian qua 🤍\n\nEm vẫn ở đây mỗi ngày 8h-21h, máy nào cũng nhận, tư vấn thật lòng chứ không ép.\n\n" + DC + "\n\n" + TAG,
"Chưa biết máy mình dán được kiểu nào? Nhắn tên máy qua " + Z + " em kiểm tra khuôn rồi tư vấn liền ạ.\n\nMiễn phí, không dán cũng không sao 😊\n\n" + TAG,
"Bảo vệ máy không phải chuyện xa xỉ, là chuyện giữ tiền của mình ạ.\n\nTUỆ TÂM PPF CNC — " + DC + "\n" + Z + "\n\n" + TAG],
}

made = 0
for day in range(1, 32):
    for si, slot in enumerate(("am", "pm")):
        idx = (day - 1) * 2 + si          # 0..61
        theme = idx % 14 + 1              # xoay vong 14 chu de
        variant = (idx // 14) % 5         # doi caption moi vong
        base = os.path.join(SRC, "ppf-%02d.png" % theme)
        name = "ppf-d%02d-%s" % (day, slot)
        shutil.copyfile(base, os.path.join(OUT, name + ".png"))
        with open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8") as f:
            f.write(CAPS[theme][variant])
        made += 1
print("Da tao %d bai (anh + caption)" % made)
