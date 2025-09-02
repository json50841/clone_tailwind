# graphytranslated.py
import re
import time
from pathlib import Path
from PIL import Image
import pytesseract
import requests

# ---------- 配置 ----------
img_file = Path(__file__).parent / "FireShot001.jpg"
output_dir = Path(__file__).parent / "Tailwind-/backend/app/vocabulary"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "translated_words.txt"

# 如果 tesseract 不在 PATH，可取消下面注释并修改路径
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


# ---------- 图片切片函数 ----------
def slice_image(img: Image.Image, max_height: int = 2000):
    slices = []
    width, height = img.size
    for top in range(0, height, max_height):
        bottom = min(top + max_height, height)
        slice_img = img.crop((0, top, width, bottom))
        slices.append(slice_img)
    return slices


# ---------- OCR 提取文字 ----------
print("📄 正在提取图片文字...")
img = Image.open(img_file)
text = ""
for slice_img in slice_image(img):
    slice_text = pytesseract.image_to_string(slice_img, lang="eng")
    text += slice_text + " "

# ---------- 提取英文单词并去重 ----------
words = re.findall(r"\b[a-zA-Z-]+\b", text)
seen = set()
unique_words = []
for w in words:
    if w.lower() not in seen:
        unique_words.append(w)
        seen.add(w.lower())

if not unique_words:
    raise ValueError("❌ 未能从图片中提取到英文单词，请检查图片文件。")


# ---------- 逐行翻译函数 ----------
def translate_word(word: str) -> str:
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": "en", "tl": "zh-CN", "dt": "t", "q": word}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        zh = response.json()[0][0][0]
        return zh
    except Exception as e:
        return f"翻译失败: {e}"


# ---------- 写入初始 TXT ----------
with open(output_file, "w", encoding="utf-8") as f:
    for idx, word in enumerate(unique_words, start=1):
        f.write(f"{idx}. {word}\n")

print(f"✅ 已提取单词，开始逐行翻译...")

# ---------- 逐行翻译并覆盖 ----------
translated_lines = []
with open(output_file, "r", encoding="utf-8") as f:
    for line in f:
        match = re.match(r"(\d+)\.\s+([a-zA-Z-]+)", line)
        if match:
            idx, word = match.groups()
            zh = translate_word(word)
            translated_lines.append(f"{idx}. {word} - {zh}\n")
            time.sleep(0.2)  # 防封
        else:
            translated_lines.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(translated_lines)

print(f"✅ 翻译完成，TXT 文件已生成: {output_file}")
