# -*- coding: utf-8 -*-
"""Chuyen file lich content markdown thanh posts.json cho Make goi qua HTTP.

Chay:  python tools/build_posts_json.py
Ket qua: posts.json o thu muc goc repo (deploy len Vercel la Make doc duoc).

Thu tu bai trong mang "posts": ngay 1 sang, ngay 1 chieu, ngay 2 sang, ngay 2 chieu, ...
Make lay bai theo cong thuc: index = ((ngay_trong_thang - 1) * 2 + (0 neu sang, 1 neu chieu)) % tong_so_bai
"""
import json
import re
import sys
from pathlib import Path

# Console Windows mac dinh la cp1252, khong in duoc tieng Viet co dau -> ep UTF-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent
THU_MUC_LICH = REPO / "media" / "lich"
WEBSITE = "https://tuetamppf.vercel.app/"
MARKDOWN_MAC_DINH = (
    REPO.parent.parent
    / "04_LICH_NOI_DUNG"
    / "Content-30-bai-TueTam-PPF-9h-17h.md"
)


# Gio mo cua moi cua tiem: 18h - 21h (truoc day la 8h - 21h).
RE_GIO_CU = re.compile(r"(?<!1)8h\s*[-–—]\s*21h")


def chuan_hoa_gio(caption: str) -> str:
    """Doi moi cach viet gio mo cua cu (8h-21h) thanh gio moi 18h - 21h."""
    caption = RE_GIO_CU.sub("18h – 21h", caption)
    caption = caption.replace("8h sáng tới 9h tối", "6h tối tới 9h tối")
    caption = caption.replace("8h sáng — 9h tối", "6h tối — 9h tối")
    return caption


def them_website(caption: str) -> str:
    """Chen dong website vao truoc cum hashtag, hoac cuoi bai neu khong co hashtag."""
    if WEBSITE in caption:
        return caption
    dong = caption.split("\n")
    vi_tri_hashtag = next(
        (i for i, d in enumerate(dong) if d.strip().startswith("#")), len(dong)
    )
    dong.insert(vi_tri_hashtag, f"🌐 {WEBSITE}")
    if vi_tri_hashtag < len(dong) - 1:
        dong.insert(vi_tri_hashtag + 1, "")
    return "\n".join(dong).strip()

# Bat dau mot ngay:  "## NGAY 12"
RE_NGAY = re.compile(r"^##\s+NG[ÀA]Y\s+(\d+)\s*$", re.IGNORECASE)
# Bat dau mot bai:   "### 9h - Bai A"  /  "### 17h - Bai B"
RE_BAI = re.compile(r"^###\s+(\d{1,2})h\s*[—\-–]\s*B[àa]i\s+([AB])\s*$", re.IGNORECASE)


def doc_cac_bai(duong_dan: Path):
    """Tra ve list dict: {ngay, buoi, gio, noi_dung}."""
    bai_viet = []
    ngay_hien_tai = None
    dang_gom = None
    dong_noi_dung = []

    def chot_bai():
        if dang_gom is None:
            return
        noi_dung = "\n".join(dong_noi_dung).strip()
        # bo dong ke ngang phan cach giua cac ngay
        noi_dung = re.sub(r"\n*^-{3,}$", "", noi_dung, flags=re.MULTILINE).strip()
        if noi_dung:
            bai_viet.append({**dang_gom, "noi_dung": noi_dung})

    for dong in duong_dan.read_text(encoding="utf-8").splitlines():
        khop_ngay = RE_NGAY.match(dong.strip())
        if khop_ngay:
            chot_bai()
            dang_gom, dong_noi_dung = None, []
            ngay_hien_tai = int(khop_ngay.group(1))
            continue

        khop_bai = RE_BAI.match(dong.strip())
        if khop_bai:
            chot_bai()
            gio = int(khop_bai.group(1))
            dang_gom = {
                "ngay": ngay_hien_tai,
                "buoi": "sang" if gio < 12 else "chieu",
                "gio": gio,
            }
            dong_noi_dung = []
            continue

        if dang_gom is not None:
            dong_noi_dung.append(dong)

    chot_bai()
    return bai_viet


def main():
    nguon = Path(sys.argv[1]) if len(sys.argv) > 1 else MARKDOWN_MAC_DINH
    dich = REPO / "posts.json"
    if nguon.exists():
        bai_viet = doc_cac_bai(nguon)
        if not bai_viet:
            sys.exit("Khong doc duoc bai nao — kiem tra lai dinh dang tieu de trong file markdown.")
        # sap xep: theo ngay, sang truoc chieu sau
        bai_viet.sort(key=lambda b: (b["ngay"], b["gio"]))
        ten_nguon = nguon.name
    elif dich.exists():
        # May khac khong co file markdown goc -> dung lai kho bai dai da luu.
        cu = json.loads(dich.read_text(encoding="utf-8"))
        bai_viet = [{"ngay": None, "gio": 0, "noi_dung": t} for t in cu.get("bai_dai", [])]
        ten_nguon = cu.get("cap_nhat", "posts.json").replace("sinh tu ", "")
        print(f"Khong thay {nguon.name} — dung lai bai_dai trong posts.json")
    else:
        sys.exit(f"Khong tim thay file content: {nguon}")

    noi_dung = [chuan_hoa_gio(b["noi_dung"]) for b in bai_viet]

    # Lich tra cuu theo ngay trong thang (1..31).
    # Uu tien caption di kem anh trong media/lich/ppf-dNN-am|pm.txt — de anh va chu
    # noi cung mot chuyen. Khong co file txt thi lay tam bai dai trong markdown.
    lich = {}
    so_khop_anh = 0
    for ngay in range(1, 32):
        muc = {}
        for buoi, hau_to, lech in (("sang", "08", 0), ("chieu", "17", 1)):
            duong_dan_txt = THU_MUC_LICH / f"ppf-d{ngay:02d}-{hau_to}.txt"
            if duong_dan_txt.exists():
                muc[buoi] = them_website(
                    chuan_hoa_gio(duong_dan_txt.read_text(encoding="utf-8").strip()))
                so_khop_anh += 1
            else:
                muc[buoi] = chuan_hoa_gio(noi_dung[(((ngay - 1) * 2) + lech) % len(noi_dung)])
        lich[str(ngay)] = muc

    ket_qua = {
        "cap_nhat": "sinh tu " + ten_nguon,
        "tong_so_bai": len(noi_dung),
        "so_caption_khop_anh": so_khop_anh,
        "website": WEBSITE,
        "anh_mau": "https://tuetamppf.vercel.app/media/lich/ppf-d{NN}-{08|17}.png",
        "lich": lich,
        "bai_dai": noi_dung,
    }

    dich.write_text(
        json.dumps(ket_qua, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Da ghi {dich}")
    print(f"  {len(bai_viet)} bai dai + {so_khop_anh} caption khop anh")


if __name__ == "__main__":
    main()
