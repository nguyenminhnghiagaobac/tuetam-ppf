# -*- coding: utf-8 -*-
"""Render cac file .html trong thu muc thanh anh .png 1080x1350 bang Chromium.

Chay:  python tools/render_png.py media/auto
Tren may khac: dat bien moi truong CHROME=/duong/dan/toi/chrome neu can.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

W, H = 1080, 1350
# Uu tien headless_shell: no cat dung 1080x1350, con chrome --headless=new
# tru mat mot phan chieu cao cho thanh cua so.
CANDIDATES = [
    os.environ.get("CHROME"),
    "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell",
    "/opt/pw-browsers/chromium",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/usr/bin/google-chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]


def chrome():
    for c in CANDIDATES:
        if c and Path(c).exists():
            return c
    sys.exit("Khong tim thay Chrome/Chromium — dat bien moi truong CHROME=...")


# Mac dinh ha bang mau 256 (file nhe gap ~6 lan, len Facebook nhin nhu nhau).
# Muon giu mau goc cho tam co anh chup that thi chay them co --net-cao.
NET_CAO = "--net-cao" in sys.argv


def co_anh_that(html_path):
    """Tam nao dung anh chup that lam nen (de chon che do nen anh)."""
    return "bgphoto{background-image" in html_path.read_text(encoding="utf-8")


def nen(path, giu_mau_that=False):
    """Giam dung luong anh xuong con ~1/6 ma mat thuong khong thay khac.

    Anh infographic it mau nen ha ve bang mau 256 mau la du dep, file nhe
    -> Vercel tai nhanh, Make ton it transfer.
    """
    try:
        from PIL import Image
    except ImportError:
        return
    im = Image.open(path).convert("RGB")
    if giu_mau_that:
        im.save(path, optimize=True)
        return
    im.quantize(colors=256, method=Image.MEDIANCUT,
                dither=Image.FLOYDSTEINBERG).save(path, optimize=True)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    src = Path(args[0] if args else "media/auto")
    exe = chrome()
    files = sorted(src.glob("*.html"))
    with tempfile.TemporaryDirectory() as profile:
        for f in files:
            out = f.with_suffix(".png")
            cmd = [exe]
            if "headless_shell" not in exe:
                cmd.append("--headless=new")
            subprocess.run(cmd + [
                "--disable-gpu", "--no-sandbox",
                "--hide-scrollbars", "--force-device-scale-factor=1",
                "--user-data-dir=" + profile,
                "--window-size=%d,%d" % (W, H),
                "--screenshot=" + str(out), f.resolve().as_uri(),
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            nen(out, NET_CAO and co_anh_that(f))
            print("  ->", out.name, "%d KB" % (out.stat().st_size // 1024))
    print("Da render %d anh" % len(files))


if __name__ == "__main__":
    main()
