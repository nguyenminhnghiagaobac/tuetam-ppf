# -*- coding: utf-8 -*-
"""Sinh bo anh infographic 1080x1080 cho fanpage Tue Tam PPF CNC Can Tho."""
import os, sys, json

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

# Chi dung THONG TIN CO THAT trong ho so cua hang. Khong bia gia, khong bia so lieu.
POSTS = [
    dict(id="01", kicker="ĐỪNG NHẦM", title="Cường lực và PPF\nKHÔNG giống nhau",
         lines=["Cường lực chỉ lo mặt kính trước.",
                "PPF ôm lưng máy, viền máy, cụm camera —",
                "mấy chỗ trầy nhiều nhất."],
         chips=["Lưng máy", "Viền máy", "Cụm camera"], theme=0),
    dict(id="02", kicker="ĐIỂM KHÁC BIỆT", title="Cắt bằng máy CNC\nchuẩn từng dòng máy",
         lines=["Rập khuôn chính xác theo model.",
                "Không rọc dao trực tiếp lên máy khách.",
                "Ôm khít viền, không hở, không bong bóng."],
         chips=["Chuẩn model", "Không rọc dao", "Ôm khít viền"], theme=1),
    dict(id="03", kicker="MỘT CHỖ LO HẾT", title="Không riêng\nđiện thoại đâu ạ",
         lines=["Điện thoại · Máy tính bảng · Laptop · Đồng hồ",
                "Máy nào cũng có khuôn cắt riêng."],
         chips=["Điện thoại", "Tablet", "Laptop", "Đồng hồ"], theme=2),
    dict(id="04", kicker="THẬT LÒNG MÀ NÓI", title="Máy trầy rồi\nbán lại bị ép giá",
         lines=["Một vết xước ở lưng máy đủ để người mua trả giá xuống.",
                "Dán từ đầu rẻ hơn nhiều so với phần bị mất giá."],
         chips=["Giữ máy như mới", "Bán lại được giá"], theme=3),
    dict(id="05", kicker="YÊN TÂM", title="Bảo hành\ntrầy xước",
         lines=["Film bị trầy trong thời gian bảo hành,",
                "anh chị cứ mang ra tiệm em xử lý."],
         chips=["Cam kết rõ ràng", "Không vòng vo"], theme=4),
    dict(id="06", kicker="GIỜ MỞ CỬA", title="8h sáng — 9h tối\nmỗi ngày",
         lines=["Anh chị đi làm về ghé vẫn kịp.",
                "Nhắn Zalo trước cho khỏi phải chờ."],
         chips=["8h - 21h", "Nhắn trước đỡ chờ"], theme=5),
    dict(id="07", kicker="COI CHỪNG", title="Dán chỗ không uy tín\nlà rước bực vào người",
         lines=["Film chợ cắt tay, hở viền, bong mép, nổi bọt khí.",
                "Gỡ ra dán lại còn mệt hơn."],
         chips=["Không hở viền", "Không bọt khí", "Không bong mép"], theme=6),
    dict(id="08", kicker="KHI NÀO NÊN DÁN?", title="4 lúc nên dán PPF\nngay và luôn",
         lines=["1. Vừa mua máy mới",
                "2. Lỡ làm rơi một lần rồi",
                "3. Trước chuyến đi xa",
                "4. Máy bắt đầu có vết xước nhỏ"],
         chips=[], theme=0),
    dict(id="09", kicker="ĐẸP TỰ NHIÊN", title="Dán rồi vẫn\nnhư máy trần",
         lines=["Film trong suốt, mỏng, ôm sát thân máy.",
                "Không làm dày máy. Không che logo.",
                "Cầm lên cảm giác y như chưa dán."],
         chips=["Trong suốt", "Không dày máy", "Không che logo"], theme=1),
    dict(id="10", kicker="GHÉ TIỆM EM", title="71 đường số 2\nkhu CBGV, P. Tân An",
         lines=["TP Cần Thơ",
                "Zalo: 0778.968.738"],
         chips=["Cần Thơ", "Mở 8h - 21h"], theme=2),
    dict(id="11", kicker="ỐP LƯNG THÌ SAO?", title="Ốp lưng che máy\nPPF cứu máy",
         lines=["Ốp dày cộm, nóng máy, mất dáng máy đẹp.",
                "PPF mỏng dính mà vẫn chống trầy.",
                "Thích thì dán PPF rồi đeo ốp cũng được."],
         chips=["Mỏng hơn ốp", "Giữ dáng máy"], theme=3),
    dict(id="12", kicker="CHỖ HAY TRẦY NHẤT", title="Cụm camera\nvà 4 góc viền",
         lines=["Đặt máy xuống bàn là camera chạm trước.",
                "Rớt nhẹ là 4 góc viền ăn đủ.",
                "Hai chỗ này PPF che được, cường lực thì không."],
         chips=["Camera", "4 góc viền"], theme=4),
    dict(id="13", kicker="TRƯỚC KHI CHỌN TIỆM", title="Hỏi 3 câu này\nlà biết chỗ ngon",
         lines=["1. Có cắt bằng máy CNC theo model không?",
                "2. Có rọc dao trực tiếp lên máy em không?",
                "3. Bảo hành thế nào nếu bong hay trầy?"],
         chips=[], theme=5),
    dict(id="14", kicker="TUỆ TÂM PPF CNC", title="Dán một lần\nyên tâm cả năm",
         lines=["Máy cắt CNC chuẩn từng model.",
                "Đa thiết bị: điện thoại, tablet, laptop, đồng hồ.",
                "Nhắn Zalo 0778.968.738 để được tư vấn."],
         chips=["CNC chuẩn model", "Đa thiết bị", "Cần Thơ"], theme=6),
]

# 7 bang mau, xoay vong cho do ngan
THEMES = [
    ("#ec0868", "#7c1fe0", "#fff5fa"),
    ("#0ea5e9", "#8b5cf6", "#f0f9ff"),
    ("#0ecb5e", "#0ea5e9", "#f0fdf6"),
    ("#f59e0b", "#ec0868", "#fffbeb"),
    ("#7c1fe0", "#0ea5e9", "#faf5ff"),
    ("#0891b2", "#0ecb5e", "#ecfeff"),
    ("#e11d48", "#f59e0b", "#fff1f2"),
]

TPL = """<meta charset="utf-8">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1080px;height:1080px;font-family:"Segoe UI",Roboto,Arial,sans-serif;
       background:%(bg)s;overflow:hidden;position:relative}
  .blob{position:absolute;border-radius:50%%;filter:blur(2px);opacity:.16}
  .b1{width:560px;height:560px;background:%(c1)s;top:-190px;right:-150px}
  .b2{width:420px;height:420px;background:%(c2)s;bottom:-160px;left:-120px}
  .wrap{position:relative;z-index:2;padding:78px 76px;height:100%%;
        display:flex;flex-direction:column}
  .kicker{display:inline-block;align-self:flex-start;font-size:26px;font-weight:800;
          letter-spacing:3px;color:#fff;padding:13px 26px;border-radius:999px;
          background:linear-gradient(100deg,%(c1)s,%(c2)s)}
  h1{margin-top:36px;font-size:%(tsize)spx;line-height:1.12;font-weight:900;
     letter-spacing:-1.5px;white-space:pre-line;
     background:linear-gradient(100deg,%(c1)s,%(c2)s);
     -webkit-background-clip:text;-webkit-text-fill-color:transparent}
  .rule{width:130px;height:9px;border-radius:9px;margin:34px 0 30px;
        background:linear-gradient(90deg,%(c1)s,%(c2)s)}
  .lines{font-size:35px;line-height:1.62;color:#243244;font-weight:500}
  .chips{margin-top:auto;display:flex;flex-wrap:wrap;gap:14px;padding-bottom:26px}
  .chip{font-size:26px;font-weight:700;color:%(c1)s;background:#fff;
        border:3px solid %(c1)s33;padding:12px 24px;border-radius:999px}
  .foot{border-top:3px solid #0000000f;padding-top:26px;display:flex;
        justify-content:space-between;align-items:flex-end}
  .brand{font-size:31px;font-weight:900;color:#16202c;letter-spacing:-.5px}
  .brand span{background:linear-gradient(100deg,%(c1)s,%(c2)s);
              -webkit-background-clip:text;-webkit-text-fill-color:transparent}
  .meta{font-size:23px;color:#5c6b7d;line-height:1.5;text-align:right;font-weight:500}
</style>
<div class="blob b1"></div><div class="blob b2"></div>
<div class="wrap">
  <div class="kicker">%(kicker)s</div>
  <h1>%(title)s</h1>
  <div class="rule"></div>
  <div class="lines">%(lines)s</div>
  <div class="chips">%(chips)s</div>
  <div class="foot">
    <div class="brand">TUỆ TÂM <span>PPF CNC</span></div>
    <div class="meta">Zalo 0778.968.738 · Mở 8h-21h<br>71 đường số 2, P. Tân An, Cần Thơ</div>
  </div>
</div>"""

manifest = []
for p in POSTS:
    c1, c2, bg = THEMES[p["theme"]]
    longest = max(len(l) for l in p["title"].split("\n"))
    tsize = 82 if longest <= 20 else (72 if longest <= 26 else 64)
    html = TPL % dict(
        c1=c1, c2=c2, bg=bg, kicker=p["kicker"], title=p["title"], tsize=tsize,
        lines="<br>".join(p["lines"]),
        chips="".join('<div class="chip">%s</div>' % c for c in p["chips"]),
    )
    name = "ppf-%s" % p["id"]
    with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    manifest.append(dict(id=p["id"], file=name + ".png", kicker=p["kicker"],
                         title=p["title"].replace("\n", " ")))

with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)
print("Da sinh %d file HTML" % len(POSTS))
