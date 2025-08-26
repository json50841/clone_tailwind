import re
from pathlib import Path
from PIL import Image
import pytesseract

# ----------------------------
# 配置
# ----------------------------
img_file = Path(__file__).parent / "FireShot001.jpg"
output_dir = Path(__file__).parent / "Tailwind-/backend/app/vocabulary"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "words_only.txt"

SLICE_HEIGHT = 1500  # 每次切块高度（避免 tesseract 卡死）


# ----------------------------
# 内存分块（顺序切）
# ----------------------------
def slice_image(img: Image.Image, max_height: int = SLICE_HEIGHT):
    width, height = img.size
    for top in range(0, height, max_height):
        bottom = min(top + max_height, height)
        yield img.crop((0, top, width, bottom))


# ----------------------------
# 主程序
# ----------------------------
def main():
    print("📄 加载图片...")
    img = Image.open(img_file)

    seen = set()
    idx = 1

    with open(output_file, "w", encoding="utf-8") as f:
        for part_idx, part in enumerate(slice_image(img), start=1):
            print(f"🔎 OCR 第 {part_idx} 块...")
            text = pytesseract.image_to_string(part, lang="eng")
            words = re.findall(r"\b[a-zA-Z-]+\b", text)

            for w in words:
                wl = w.lower()
                if wl not in seen:
                    f.write(f"{idx}. {w}\n")
                    seen.add(wl)
                    idx += 1

    print(f"✅ 单词提取完成，结果保存在: {output_file}")


if __name__ == "__main__":
    main()
