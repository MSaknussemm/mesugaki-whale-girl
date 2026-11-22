#!/usr/bin/env python3
"""生成 preview/overview.png —— 每段动画取第 1.2 秒（不足 1.2 秒取中段）拼成总览图。

用法：
    python tools/make_preview.py characters/mesugaki/videos preview/overview.png

依赖：ffmpeg（含 libvpx-vp9 解码器）、Pillow。

版式（与 v1.2.x 一致）：
    ｜ 9 列 × N 行，格子 240×135 缩略图 + 20 px 标签条
    ｜ 缩略图背景透明（PNG alpha），标签条 rgb(40,40,52) + 白字
    ｜ 分类顺序 idle → random → click → move → turn → drag → events，同类按 Unicode 排序
"""

import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

COLS = 9
THUMB_W, THUMB_H = 240, 135
LABEL_H = 20
NAME_H = 155
SAMPLE_AT = 1.2
CATEGORY_ORDER = ["idle", "random", "click", "move", "turn", "drag", "events"]
BAR_COLOR = (40, 40, 52)

FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
FFPROBE = os.environ.get("FFPROBE", "ffprobe")


def duration(path):
    out = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def grab(path, dst):
    """按 VP9 原生解码器取一帧，保留 alpha 平面。"""
    at = SAMPLE_AT
    try:
        d = duration(path)
        if d < SAMPLE_AT:
            at = d / 2.0
    except Exception:
        d = None
    cmd = [FFMPEG, "-y", "-v", "error", "-ss", f"{at:.3f}", "-c:v", "libvpx-vp9",
           "-i", path, "-frames:v", "1", "-pix_fmt", "rgba", dst]
    subprocess.run(cmd, capture_output=True, check=True)
    return dst


def load_font(size=12):
    for name in ("msyh.ttc", "msyhbd.ttc", "simhei.ttf", "arial.ttf"):
        for base in (os.environ.get("WINDIR", r"C:\Windows"), "/usr/share/fonts"):
            p = os.path.join(base, "Fonts" if base.startswith("C:") else "", name)
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except Exception:
                    pass
    return ImageFont.load_default()


def collect(videos_dir):
    items = []
    for cat in CATEGORY_ORDER:
        d = os.path.join(videos_dir, cat)
        if not os.path.isdir(d):
            continue
        names = sorted(
            f for f in os.listdir(d)
            if f.lower().endswith((".webm", ".mp4"))
        )
        for n in names:
            items.append((cat, n, os.path.join(d, n)))
    return items


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    videos_dir, out_path = sys.argv[1], sys.argv[2]
    items = collect(videos_dir)
    if not items:
        print("没有找到任何片段", file=sys.stderr)
        return 1

    rows = (len(items) + COLS - 1) // COLS
    sheet = Image.new("RGBA", (COLS * THUMB_W, rows * NAME_H), (0, 0, 0, 0))
    font = load_font(12)
    draw = ImageDraw.Draw(sheet)

    tmp = tempfile.mkdtemp(prefix="preview-")
    for i, (cat, name, path) in enumerate(items):
        cx, cy = i % COLS, i // COLS
        x, y = cx * THUMB_W, cy * NAME_H
        png = os.path.join(tmp, f"{i:03d}.png")
        try:
            grab(path, png)
            with Image.open(png) as im:
                im = im.convert("RGBA")
                if im.size != (THUMB_W, THUMB_H):
                    im = im.resize((THUMB_W, THUMB_H), Image.LANCZOS)
                sheet.alpha_composite(im, (x, y))
        except Exception as exc:  # 单段失败不拖垮整张图
            print(f"! {cat}/{name}: {exc}", file=sys.stderr)
        draw.rectangle([x, y + THUMB_H, x + THUMB_W - 1, y + NAME_H - 1], fill=BAR_COLOR)
        draw.text((x + 3, y + THUMB_H + 4), f"{cat}/{os.path.splitext(name)[0]}",
                  font=font, fill=(255, 255, 255, 255))
        if (i + 1) % 10 == 0:
            print(f"  {i + 1}/{len(items)}", file=sys.stderr)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    sheet.save(out_path, "PNG", optimize=True)
    print(f"{len(items)} 段 -> {out_path} ({sheet.size[0]}x{sheet.size[1]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
