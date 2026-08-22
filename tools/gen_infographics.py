# -*- coding: utf-8 -*-
"""Sinh bo anh infographic 1080x1350 (4:5) cho fanpage Tue Tam PPF CNC Can Tho.

Chay:
    python tools/gen_infographics.py media/auto      # sinh file .html
    python tools/render_png.py     media/auto        # render ra .png

Muon dung ANH THAT thay cho hinh ve minh hoa: bo anh vao thu muc
media/thuc-te/ voi ten trung id cua bai, vi du media/thuc-te/04.jpg
(chap nhan .jpg .jpeg .png .webp). Co anh that thi generator tu dong
uu tien anh that, khong co thi ve mockup thiet bi bang SVG.

Chi dung THONG TIN CO THAT trong ho so cua hang. Khong bia gia, khong bia so lieu.
"""
import base64
import json
import mimetypes
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FONT_DIR = REPO / "tools" / "fonts"
PHOTO_DIR = REPO / "media" / "thuc-te"

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else REPO / "media" / "auto")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1350

ZALO = "0778.968.738"
ADDR = "71 đường số 2, khu CBGV, P. Tân An, Cần Thơ"
HOURS = "Mở cửa 18h – 21h mỗi ngày"

# ---------------------------------------------------------------- bang mau
# Mau dam, tuoi, do tuong phan cao — nhin tren feed dien thoai la bat mat ngay.
THEMES = [
    dict(c1="#ff2d78", c2="#7b18e0", ac="#ffd60a", soft="#ff9ec7"),  # hong -> tim
    dict(c1="#0ea5e9", c2="#1e3a8a", ac="#ffd60a", soft="#7dd3fc"),  # xanh duong
    dict(c1="#00c853", c2="#0369a1", ac="#eaff00", soft="#86efac"),  # xanh la -> xanh
    dict(c1="#f59e0b", c2="#dc2626", ac="#00e5ff", soft="#fed7aa"),  # cam -> do
    dict(c1="#7c3aed", c2="#2563eb", ac="#ffd60a", soft="#c4b5fd"),  # tim -> xanh
    dict(c1="#06b6d4", c2="#059669", ac="#eaff00", soft="#a7f3d0"),  # cyan -> luc
    dict(c1="#e11d48", c2="#7c2d12", ac="#ffd60a", soft="#fda4af"),  # do -> nau do
]


def font_face():
    """Nhung font Be Vietnam Pro (OFL) truc tiep tu tools/fonts."""
    css = []
    for w in (400, 600, 700, 800, 900):
        f = FONT_DIR / ("BeVietnamPro-%d.ttf" % w)
        if not f.exists():
            continue
        b64 = base64.b64encode(f.read_bytes()).decode()
        css.append(
            "@font-face{font-family:'BVP';font-style:normal;font-weight:%d;"
            "src:url(data:font/ttf;base64,%s) format('truetype')}" % (w, b64)
        )
    return "".join(css)


def data_uri(path):
    path = Path(path)
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    return "data:%s;base64,%s" % (mime, base64.b64encode(path.read_bytes()).decode())


def anh_that(post_id):
    """Tra ve data-uri cua anh that neu chu tiem da bo vao media/thuc-te/."""
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = PHOTO_DIR / (post_id + ext)
        if p.exists():
            return data_uri(p)
    return None


# ---------------------------------------------------------- mockup thiet bi
def _defs(uid, dark=True):
    a, b, c = ("#39435a", "#0f172a", "#4b5563") if dark else ("#e5e7eb", "#94a3b8", "#f8fafc")
    return (
        '<defs>'
        '<linearGradient id="bd%s" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="%s"/><stop offset=".55" stop-color="%s"/>'
        '<stop offset="1" stop-color="%s"/></linearGradient>'
        '<linearGradient id="gl%s" x1="0" y1="0" x2=".9" y2="1">'
        '<stop offset="0" stop-color="#fff" stop-opacity=".38"/>'
        '<stop offset=".45" stop-color="#fff" stop-opacity=".04"/>'
        '<stop offset="1" stop-color="#fff" stop-opacity=".16"/></linearGradient>'
        '<linearGradient id="fm%s" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffffff" stop-opacity=".62"/>'
        '<stop offset=".5" stop-color="#dffcff" stop-opacity=".30"/>'
        '<stop offset="1" stop-color="#ffffff" stop-opacity=".58"/></linearGradient>'
        '</defs>' % (uid, a, b, c, uid, uid)
    )


def svg_phone(uid="p", scratch=False, peel=True, camera=True):
    peel_path = (
        '<path d="M330 660 L330 470 Q250 520 196 596 Q170 632 160 660 Z" fill="url(#fm%s)"/>'
        '<path d="M330 470 Q250 520 196 596 Q170 632 160 660" fill="none" '
        'stroke="#ffffff" stroke-opacity=".85" stroke-width="5"/>' % uid
        if peel else ""
    )
    scr = (
        '<path d="M92 300 L246 420" stroke="#ffffff" stroke-opacity=".55" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M120 470 L206 512" stroke="#ffffff" stroke-opacity=".38" stroke-width="4" stroke-linecap="round"/>'
        if scratch else ""
    )
    cam = (
        '<rect x="52" y="52" width="168" height="168" rx="48" fill="#0b1220" fill-opacity=".92"/>'
        '<circle cx="104" cy="104" r="31" fill="#1f2937" stroke="#64748b" stroke-width="4"/>'
        '<circle cx="168" cy="104" r="31" fill="#1f2937" stroke="#64748b" stroke-width="4"/>'
        '<circle cx="104" cy="168" r="31" fill="#1f2937" stroke="#64748b" stroke-width="4"/>'
        '<circle cx="96" cy="96" r="10" fill="#93c5fd" fill-opacity=".8"/>'
        '<circle cx="160" cy="96" r="10" fill="#93c5fd" fill-opacity=".8"/>'
        '<circle cx="176" cy="168" r="14" fill="#fde68a" fill-opacity=".85"/>'
        if camera else ""
    )
    return (
        '<svg viewBox="0 0 340 680" class="dev">%s'
        '<rect x="12" y="12" width="316" height="656" rx="62" fill="url(#bd%s)"/>'
        '<rect x="12" y="12" width="316" height="656" rx="62" fill="url(#gl%s)"/>'
        '%s%s%s'
        '<rect x="12" y="12" width="316" height="656" rx="62" fill="none" '
        'stroke="#ffffff" stroke-opacity=".28" stroke-width="4"/></svg>'
        % (_defs(uid), uid, uid, cam, scr, peel_path)
    )


def svg_tablet(uid="t", peel=True):
    peel_path = (
        '<path d="M470 620 L470 470 Q392 512 344 578 Q322 604 314 620 Z" fill="url(#fm%s)"/>'
        '<path d="M470 470 Q392 512 344 578 Q322 604 314 620" fill="none" '
        'stroke="#fff" stroke-opacity=".85" stroke-width="5"/>' % uid
        if peel else ""
    )
    return (
        '<svg viewBox="0 0 490 640" class="dev">%s'
        '<rect x="14" y="14" width="462" height="612" rx="40" fill="url(#bd%s)"/>'
        '<rect x="14" y="14" width="462" height="612" rx="40" fill="url(#gl%s)"/>'
        '<rect x="46" y="46" width="112" height="112" rx="32" fill="#0b1220" fill-opacity=".92"/>'
        '<circle cx="86" cy="86" r="24" fill="#1f2937" stroke="#64748b" stroke-width="4"/>'
        '<circle cx="128" cy="128" r="14" fill="#fde68a" fill-opacity=".8"/>'
        '%s<rect x="14" y="14" width="462" height="612" rx="40" fill="none" '
        'stroke="#fff" stroke-opacity=".28" stroke-width="4"/></svg>'
        % (_defs(uid), uid, uid, peel_path)
    )


def svg_laptop(uid="l", peel=True):
    peel_path = (
        '<path d="M596 300 L596 176 Q520 214 476 268 Q458 290 452 300 Z" fill="url(#fm%s)"/>'
        '<path d="M596 176 Q520 214 476 268 Q458 290 452 300" fill="none" '
        'stroke="#fff" stroke-opacity=".85" stroke-width="5"/>' % uid
        if peel else ""
    )
    return (
        '<svg viewBox="0 0 700 470" class="dev">%s'
        '<rect x="52" y="18" width="596" height="382" rx="26" fill="url(#bd%s)"/>'
        '<rect x="52" y="18" width="596" height="382" rx="26" fill="url(#gl%s)"/>'
        '<rect x="86" y="52" width="528" height="314" rx="12" fill="#0b1220" fill-opacity=".55"/>'
        '<circle cx="350" cy="35" r="6" fill="#64748b"/>'
        '%s'
        '<path d="M8 400 H692 L664 452 H36 Z" fill="url(#bd%s)"/>'
        '<path d="M8 400 H692 L664 452 H36 Z" fill="url(#gl%s)"/>'
        '<rect x="286" y="416" width="128" height="12" rx="6" fill="#0b1220" fill-opacity=".5"/>'
        '</svg>' % (_defs(uid), uid, uid, peel_path, uid, uid)
    )


def svg_watch(uid="w"):
    return (
        '<svg viewBox="0 0 300 470" class="dev">%s'
        '<path d="M96 8 H204 L214 118 H86 Z" fill="#334155"/>'
        '<path d="M86 352 H214 L204 462 H96 Z" fill="#334155"/>'
        '<rect x="52" y="104" width="196" height="262" rx="62" fill="url(#bd%s)"/>'
        '<rect x="52" y="104" width="196" height="262" rx="62" fill="url(#gl%s)"/>'
        '<rect x="76" y="128" width="148" height="214" rx="46" fill="#0b1220" fill-opacity=".72"/>'
        '<rect x="246" y="182" width="16" height="46" rx="8" fill="#64748b"/>'
        '</svg>' % (_defs(uid), uid, uid)
    )


DEVICES = {
    "phone": lambda: svg_phone("a"),
    "phone-scratch": lambda: svg_phone("b", scratch=True, peel=False),
    "phone-cam": lambda: svg_phone("c", peel=False),
    "tablet": lambda: svg_tablet("d"),
    "laptop": lambda: svg_laptop("e"),
    "watch": lambda: svg_watch("f"),
    "combo": lambda: (
        '<div class="combo">%s%s%s%s</div>'
        % (svg_laptop("g", peel=False), svg_tablet("h", peel=False),
           svg_phone("i", peel=False), svg_watch("j"))
    ),
}


# ------------------------------------------------------------- noi dung bai
# [[...]] = phan duoc to sang trong tieu de
POSTS = [
    dict(id="01", theme=0, layout="hero", device="phone",
         kicker="ĐỪNG NHẦM NỮA", emoji="⚠️",
         title="Cường lực KHÔNG\ncứu nổi [[lưng máy]]",
         lines=["Cường lực chỉ giữ mặt kính trước.",
                "Lưng máy · viền · cụm camera — mấy chỗ trầy",
                "nhiều nhất — thì bỏ trống hoàn toàn."],
         chips=["Lưng máy", "4 góc viền", "Cụm camera"]),

    dict(id="02", theme=1, layout="compare",
         kicker="ĐIỂM KHÁC BIỆT", emoji="🎯",
         title="Khuôn CNC chuẩn\n[[từng dòng máy]]",
         bad_title="Cắt tay ước chừng",
         bad=["Rọc dao ngay trên máy khách", "Lệch viền, lố qua camera", "Mép cong, bám bụi"],
         good_title="Cắt CNC theo model",
         good=["Film cắt sẵn, dao không chạm máy", "Ôm khít từng đường viền", "Đặt lên là vừa, không cắt gọt"],
         chips=["Chuẩn model", "Không rọc dao", "Ôm khít viền"]),

    dict(id="03", theme=2, layout="hero", device="combo",
         kicker="MỘT CHỖ LO HẾT", emoji="💯",
         title="Máy nào ở nhà\n[[cũng dán được]]",
         lines=["Điện thoại · Máy tính bảng · Laptop · Đồng hồ.",
                "Mỗi loại một khuôn cắt riêng, đem một lần dán hết."],
         chips=["Điện thoại", "Tablet", "Laptop", "Đồng hồ"]),

    dict(id="04", theme=3, layout="hero", device="laptop",
         kicker="DÂN VĂN PHÒNG ƠI", emoji="💻",
         title="Laptop trầy nắp là\n[[rớt giá thấy rõ]]",
         lines=["Nắp lưng, chiếu nghỉ tay, viền màn hình —",
                "3 chỗ xuống cấp nhanh nhất sau vài tháng.",
                "PPF phủ trong suốt, gõ phím vẫn êm như cũ."],
         chips=["Nắp lưng", "Chiếu nghỉ tay", "Viền máy"]),

    dict(id="05", theme=4, layout="hero", device="tablet",
         kicker="MÁY TÍNH BẢNG", emoji="📱",
         title="Lưng nhôm trầy rồi\n[[hết đường cứu]]",
         lines=["Để bàn, bỏ balo, dựng bao da — vẫn trầy như thường.",
                "Đánh bóng không về như cũ được đâu ạ.",
                "Dán lưng + viền một lần, xài mấy năm vẫn đẹp."],
         chips=["Lưng máy", "Viền máy", "Cụm camera"]),

    dict(id="06", theme=6, layout="hero", device="phone-scratch",
         kicker="TIỀN TƯƠI CHỨ ĐÂU", emoji="💰",
         title="Lưng trầy vài vết,\nbán lại [[bị ép giá]]",
         lines=["Người mua lật lưng máy coi đầu tiên, không coi màn.",
                "Miếng film dán từ đầu rẻ hơn phần bị trừ giá rất nhiều."],
         chips=["Giữ máy như mới", "Bán lại được giá"]),

    dict(id="07", theme=5, layout="policy",
         kicker="NÓI RÕ TỪ ĐẦU", emoji="🛡️",
         title="Bảo hành\n[[lỗi kỹ thuật]]",
         good_title="CÓ bảo hành",
         good=["Nổi bọt khí sau khi dán", "Bong tróc, hở mép, lệch viền",
               "Mọi lỗi do người dán gây ra"],
         bad_title="KHÔNG bảo hành",
         bad=["Trầy xước trong quá trình sử dụng", "Va đập, rơi rớt, cấn móp",
              "Tự gỡ film ra dán lại"],
         note="Film sinh ra để chịu trầy thay cho máy — trầy trên film là chuyện bình thường ạ."),

    dict(id="08", theme=0, layout="hours",
         kicker="GIỜ MỞ CỬA MỚI", emoji="🕕",
         title="Tối [[18h – 21h]]\nmỗi ngày",
         lines=["Ban ngày em vẫn nhận đặt lịch qua Zalo.",
                "Tối ghé là dán liền, ngồi chờ lấy máy về luôn."],
         chips=["18h – 21h", "Đặt lịch Zalo cả ngày"]),

    dict(id="09", theme=3, layout="compare",
         kicker="COI CHỪNG TIỀN MẤT", emoji="😤",
         title="Ham rẻ dán ẩu,\n[[gỡ ra còn cực hơn]]",
         bad_title="Dấu hiệu dán ẩu",
         bad=["Hở viền, lòi phần máy trần", "Bọt khí li ti không tan",
              "Mép film cong lên bám bụi"],
         good_title="Ở Tuệ Tâm",
         good=["Film cắt CNC đúng khuôn model", "Dán phòng kín, kiểm tra trước khi giao",
               "Lỗi thi công → làm lại miễn phí"],
         chips=["Không hở viền", "Không bọt khí", "Không bong mép"]),

    dict(id="10", theme=1, layout="list",
         kicker="DÁN LÚC NÀO?", emoji="⏰",
         title="4 thời điểm\n[[nên dán ngay]]",
         items=["Vừa bóc hộp máy mới — lúc máy còn nguyên vẹn nhất",
                "Vừa lỡ làm rơi một lần — lần sau chưa chắc còn hên",
                "Trước chuyến đi xa — máy va quẹt nhiều hơn ngày thường",
                "Máy mới chớm xước — đừng để vết đó lan thêm"]),

    dict(id="11", theme=2, layout="hero", device="phone",
         kicker="ĐẸP TỰ NHIÊN", emoji="✨",
         title="Dán xong vẫn\n[[như máy trần]]",
         lines=["Film trong suốt, mỏng, ôm sát thân máy.",
                "Không làm dày máy · không che logo · không ám vàng.",
                "Thích đeo ốp thêm cũng không bị kênh."],
         chips=["Trong suốt", "Mỏng nhẹ", "Không che logo"]),

    dict(id="12", theme=4, layout="address",
         kicker="GHÉ TIỆM EM NHA", emoji="📍",
         title="71 đường số 2,\n[[khu CBGV]]",
         lines=["P. Tân An, TP Cần Thơ", "Mở cửa 18h – 21h mỗi ngày"],
         chips=["Cần Thơ", "18h – 21h"]),

    dict(id="13", theme=5, layout="compare",
         kicker="ỐP HAY PPF?", emoji="🤔",
         title="Ốp chỉ che máy,\nPPF [[cứu máy]]",
         bad_title="Ốp lưng",
         bad=["Dày cộm, mất dáng máy đẹp", "Bụi lọt vô trong ốp mài xước lưng",
              "Tháo ốp ra là máy trần hoàn toàn"],
         good_title="PPF",
         good=["Mỏng dính, ôm sát thân máy", "Chống trầy 24/7, không cần tháo",
               "Dán rồi vẫn đeo ốp bình thường"],
         chips=["Mỏng hơn ốp", "Giữ dáng máy"]),

    dict(id="14", theme=6, layout="hero", device="phone-cam",
         kicker="CHỖ TRẦY SỚM NHẤT", emoji="📸",
         title="Cụm camera và\n[[4 góc viền]]",
         lines=["Đặt máy xuống bàn là cụm camera chạm trước tiên.",
                "Camera trầy → hình mờ, loá khi chụp ngược sáng.",
                "Thay cụm camera tốn gấp nhiều lần miếng film."],
         chips=["Camera", "4 góc viền", "Cạnh máy"]),

    dict(id="15", theme=0, layout="list",
         kicker="TRƯỚC KHI GIAO MÁY", emoji="🔍",
         title="Hỏi 3 câu này\n[[là biết tiệm ngon]]",
         items=["Có cắt bằng máy CNC theo đúng model máy em không?",
                "Có rọc dao trực tiếp lên máy khách không?",
                "Bảo hành ra sao nếu film nổi bọt, bong tróc?"]),

    dict(id="16", theme=1, layout="cta",
         kicker="BÁO GIÁ NHANH", emoji="⚡",
         title="Nhắn tên máy,\n[[em báo giá liền]]",
         lines=["Tư vấn miễn phí — không dán cũng không sao ạ.",
                "Em kiểm tra có sẵn khuôn cắt cho máy anh chị chưa."],
         chips=["Điện thoại", "Tablet", "Laptop", "Đồng hồ"]),
]


# --------------------------------------------------------------- giao dien
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:%(W)dpx;height:%(H)dpx;font-family:'BVP','Be Vietnam Pro',
     'Segoe UI',Roboto,Arial,sans-serif;overflow:hidden;position:relative;
     background:linear-gradient(152deg,%(c1)s 0%%,%(c2)s 100%%);color:#fff}
.bg{position:absolute;inset:0;overflow:hidden}
.blob{position:absolute;border-radius:50%%}
.b1{width:760px;height:760px;top:-320px;right:-260px;
    background:radial-gradient(circle at 30%% 30%%,#ffffff5c,#ffffff00 68%%)}
.b2{width:620px;height:620px;bottom:-280px;left:-220px;
    background:radial-gradient(circle at 50%% 50%%,%(soft)s6b,#ffffff00 70%%)}
.b3{width:300px;height:300px;top:44%%;left:-140px;
    background:radial-gradient(circle,%(ac)s3d,#ffffff00 70%%)}
.dots{position:absolute;inset:0;opacity:.16;
      background-image:radial-gradient(#fff 2.4px,transparent 2.4px);
      background-size:38px 38px}
.ray{position:absolute;width:1500px;height:190px;top:-120px;left:-260px;
     transform:rotate(-24deg);background:linear-gradient(90deg,#ffffff00,#ffffff2e,#ffffff00)}
.card{position:relative;z-index:3;height:100%%;padding:52px 60px 236px;
      display:flex;flex-direction:column;overflow:hidden}
.top{display:flex;align-items:center;gap:14px;font-size:25px;font-weight:800;
     letter-spacing:2.5px;opacity:.95}
.top .dot{width:13px;height:13px;border-radius:50%%;background:%(ac)s;
          box-shadow:0 0 0 7px %(ac)s2e}
.kick{flex:none;align-self:flex-start;margin-top:22px;font-size:30px;font-weight:900;
      letter-spacing:2.5px;color:#10151f;background:%(ac)s;padding:15px 30px;
      border-radius:999px;box-shadow:0 14px 34px #00000038;
      display:flex;align-items:center;gap:12px}
h1{margin-top:22px;font-size:%(tsize)dpx;line-height:1.08;font-weight:900;
   letter-spacing:-2px;white-space:pre-line;text-shadow:0 8px 30px #00000042}
.hl{color:%(ac)s;position:relative;white-space:nowrap}
.hl:after{content:"";position:absolute;left:-4px;right:-4px;bottom:2px;height:14px;
          border-radius:8px;background:%(ac)s;opacity:.26;z-index:-1}
.mid{flex:1 1 0;display:flex;flex-direction:column;justify-content:center;
     align-items:center;min-height:0;overflow:hidden;padding:18px 0 4px}
.lines{font-size:33px;line-height:1.55;font-weight:500;opacity:.97;
       text-shadow:0 3px 14px #0000002e}
.lines.left{align-self:flex-start;margin-top:4px}
.dev{filter:drop-shadow(0 34px 54px rgba(0,0,0,.42))}
.stage{flex:1 1 0;display:flex;align-items:center;justify-content:center;
       gap:26px;width:100%%;min-height:0;overflow:hidden;padding-top:12px}
.stage .dev{max-height:100%%;height:100%%;width:auto;min-height:0}
.stage img.photo{min-height:0}
.combo{display:flex;align-items:flex-end;justify-content:center;gap:22px;
       height:100%%;width:100%%}
.combo .dev{height:auto}
.combo svg:nth-child(1){width:44%%}
.combo svg:nth-child(2){width:20%%}
.combo svg:nth-child(3){width:15%%}
.combo svg:nth-child(4){width:11%%}
.photo{border-radius:34px;border:9px solid #fff;box-shadow:0 30px 60px #00000059;
       max-height:100%%;max-width:100%%;object-fit:cover;transform:rotate(-1.6deg)}
.chips{display:flex;flex-wrap:wrap;gap:13px;margin:18px 0 16px;flex:none}
.chip{font-size:25px;font-weight:800;color:#fff;background:#ffffff2b;
      border:3px solid #ffffff5c;padding:12px 24px;border-radius:999px;
      backdrop-filter:blur(3px)}
.foot{position:absolute;left:60px;right:60px;bottom:46px;
      background:#fff;border-radius:30px;padding:22px 28px;display:flex;
      justify-content:space-between;align-items:center;gap:18px;
      box-shadow:0 20px 44px #00000038}
.brand{font-size:33px;font-weight:900;color:#0d1522;letter-spacing:-.6px;line-height:1.15}
.brand span{color:%(c1)s}
.brand small{display:block;font-size:21px;font-weight:700;color:#64748b;letter-spacing:1.6px}
.fmeta{text-align:right;font-size:23px;font-weight:600;color:#3f4c5f;line-height:1.5}
.fmeta b{display:block;font-size:29px;font-weight:900;color:#0d1522}
/* --- compare / policy --- */
.cmp{display:flex;gap:20px;width:100%%;flex:0 1 auto;min-height:0;align-items:stretch}
.pan{flex:1;background:#ffffff1f;border:3px solid #ffffff40;border-radius:30px;
     padding:28px 26px;display:flex;flex-direction:column;gap:16px;backdrop-filter:blur(3px)}
.pan.no{background:#0000002e;border-color:#ffffff33}
.pan.yes{background:#ffffff26;border-color:%(ac)s99}
.pan h3{font-size:31px;font-weight:900;display:flex;align-items:center;gap:12px;
        letter-spacing:-.4px}
.pan.yes h3{color:%(ac)s}
.pan li{list-style:none;font-size:26px;line-height:1.42;font-weight:600;
        display:flex;gap:12px;opacity:.97}
.pan li:before{content:"—";opacity:.6}
.pan.no li:before{content:"✕";color:#ff9d9d;font-weight:900}
.pan.yes li:before{content:"✓";color:%(ac)s;font-weight:900}
.note{margin-top:18px;font-size:26px;font-weight:600;line-height:1.5;opacity:.95;
      background:#ffffff1f;border-left:8px solid %(ac)s;border-radius:14px;padding:18px 22px}
/* --- list --- */
.items{display:flex;flex-direction:column;gap:18px;width:100%%;flex:none}
.item{display:flex;gap:22px;align-items:center;background:#ffffff21;
      border:3px solid #ffffff3d;border-radius:26px;padding:24px 26px}
.num{flex:none;width:66px;height:66px;border-radius:20px;background:%(ac)s;color:#10151f;
     font-size:34px;font-weight:900;display:flex;align-items:center;justify-content:center}
.item p{font-size:28px;font-weight:700;line-height:1.35}
/* --- hours / cta --- */
.big{font-size:120px;font-weight:900;letter-spacing:-4px;line-height:1;
     color:%(ac)s;text-shadow:0 10px 34px #00000047}
.zbox{width:100%%;background:#ffffff26;border:4px dashed #ffffff70;border-radius:32px;
      padding:30px;text-align:center}
.zbox .lbl{font-size:27px;font-weight:800;letter-spacing:3px;opacity:.9}
.zbox .num2{font-size:78px;font-weight:900;letter-spacing:-2px;color:%(ac)s;margin-top:6px}
"""

TPL = """<meta charset="utf-8"><style>%(font)s%(css)s</style>
<div class="bg"><div class="ray"></div><div class="dots"></div>
<div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div></div>
<div class="card">
  <div class="top"><span class="dot"></span>TUỆ TÂM PPF CNC · CẦN THƠ</div>
  <div class="kick"><span>%(emoji)s</span>%(kicker)s</div>
  <h1>%(title)s</h1>
  <div class="mid">%(body)s</div>
  %(chips)s
  <div class="foot">
    <div class="brand">TUỆ TÂM <span>PPF CNC</span><small>CẮT CNC CHUẨN MODEL</small></div>
    <div class="fmeta"><b>Zalo %(zalo)s</b>%(hours)s<br>%(addr)s</div>
  </div>
</div>"""


def _hl(text):
    return text.replace("[[", '<span class="hl">').replace("]]", "</span>")


def _plain(text):
    return text.replace("[[", "").replace("]]", "").replace("\n", " ")


def _chips(post):
    if not post.get("chips"):
        return ""
    return '<div class="chips">%s</div>' % "".join(
        '<div class="chip">%s</div>' % c for c in post["chips"]
    )


def _lines(post, cls="lines left"):
    if not post.get("lines"):
        return ""
    return '<div class="%s">%s</div>' % (cls, "<br>".join(post["lines"]))


def _panel(kind, title, items):
    return '<div class="pan %s"><h3>%s</h3>%s</div>' % (
        kind, title, "".join("<li>%s</li>" % i for i in items)
    )


def build_body(post):
    lay = post["layout"]
    photo = anh_that(post["id"])

    if lay in ("hero", "cta"):
        if photo:
            visual = '<div class="stage"><img class="photo" src="%s"></div>' % photo
        elif lay == "cta":
            visual = '<div class="stage">%s</div>' % DEVICES["combo"]()
        else:
            visual = '<div class="stage">%s</div>' % DEVICES[post["device"]]()
        extra = ('<div class="zbox"><div class="lbl">NHẮN ZALO</div>'
                 '<div class="num2">%s</div></div>' % ZALO) if lay == "cta" else ""
        return _lines(post) + visual + extra

    if lay in ("compare", "policy"):
        # Bai bao hanh: dua ve "CO bao hanh" len truoc cho de doc.
        thu_tu = [("yes", "good"), ("no", "bad")] if lay == "policy" else [
            ("no", "bad"), ("yes", "good")]
        cmp_html = '<div class="cmp">%s</div>' % "".join(
            _panel(kind, post[key + "_title"], post[key]) for kind, key in thu_tu)
        note = '<div class="note">%s</div>' % post["note"] if post.get("note") else ""
        return cmp_html + note

    if lay == "list":
        items = "".join(
            '<div class="item"><div class="num">%d</div><p>%s</p></div>' % (i + 1, t)
            for i, t in enumerate(post["items"])
        )
        return '<div class="items">%s</div>' % items

    if lay in ("hours", "address"):
        src = photo or data_uri(REPO / "media" / "mat-tien.jpg")
        big = '<div class="big">18h – 21h</div>' if lay == "hours" else ""
        return (_lines(post) + big +
                '<div class="stage"><img class="photo" src="%s"></div>' % src)

    raise ValueError("layout la: " + lay)


def main():
    font = font_face()
    manifest = []
    for p in POSTS:
        th = THEMES[p["theme"]]
        longest = max(len(_plain(l)) for l in p["title"].split("\n"))
        tsize = 92 if longest <= 18 else (82 if longest <= 24 else 72)
        css = CSS % dict(W=W, H=H, tsize=tsize, **th)
        html = TPL % dict(
            font=font, css=css, emoji=p["emoji"], kicker=p["kicker"],
            title=_hl(p["title"]), body=build_body(p), chips=_chips(p),
            zalo=ZALO, hours=HOURS, addr=ADDR,
        )
        name = "ppf-%s" % p["id"]
        (OUT / (name + ".html")).write_text(html, encoding="utf-8")
        manifest.append(dict(id=p["id"], file=name + ".png", kicker=p["kicker"],
                             title=_plain(p["title"]), layout=p["layout"],
                             anh_that=bool(anh_that(p["id"]))))

    (OUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("Da sinh %d file HTML trong %s" % (len(POSTS), OUT))


if __name__ == "__main__":
    main()
