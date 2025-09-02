# transform_pdf_to_txt_final.py
import re
import requests
import time
from pathlib import Path
from PyPDF2 import PdfReader

# ----------------------------
# 配置 PDF 文件和输出路径
# ----------------------------
pdf_file = Path(__file__).parent / "test.pdf"
output_dir = Path(__file__).parent / "Tailwind-/backend/app/vocabulary"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "translated_words.txt"

# ----------------------------
# 提取 PDF 文本（处理复杂排版）
# ----------------------------
reader = PdfReader(str(pdf_file))
text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        # 替换换行符，保留空格分隔单词
        page_text = page_text.replace("\n", " ")
        text += page_text + " "

# ----------------------------
# 提取英文单词（字母和可选连字符）
# ----------------------------
words = re.findall(r"\b[a-zA-Z-]+\b", text)
# 去重并保持顺序
seen = set()
unique_words = []
for w in words:
    lw = w.lower()
    if lw not in seen:
        unique_words.append(w)
        seen.add(lw)

if not unique_words:
    raise ValueError("❌ 没有从 PDF 提取到单词，请检查 PDF 内容")

print(f"提取到 {len(unique_words)} 个单词，开始翻译...")


# ----------------------------
# 批量翻译函数
# ----------------------------
def batch_translate(words_list, batch_size=50, delay=0.3):
    """
    批量翻译单词
    :param words_list: 单词列表
    :param batch_size: 每次请求数量
    :param delay: 每批请求间隔，防止被封
    """
    results = []
    for i in range(0, len(words_list), batch_size):
        chunk = words_list[i : i + batch_size]
        query = " ".join(chunk)
        try:
            url = "https://translate.googleapis.com/translate_a/single"
            params = {"client": "gtx", "sl": "en", "tl": "zh-CN", "dt": "t", "q": query}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            translations = response.json()[0]
            # Google 返回的是每个单词的翻译
            chunk_results = [t[0] for t in translations[: len(chunk)]]
            results.extend(chunk_results)
        except Exception as e:
            # 如果请求失败，用提示代替
            results.extend([f"翻译失败: {e}"] * len(chunk))
        time.sleep(delay)
    return results


# ----------------------------
# 执行翻译
# ----------------------------
translations = batch_translate(unique_words)

# ----------------------------
# 写入 TXT 文件
# ----------------------------
with open(output_file, "w", encoding="utf-8") as f:
    for idx, (en, zh) in enumerate(zip(unique_words, translations), start=1):
        f.write(f"{idx}. {en} - {zh}\n")

print(f"✅ 翻译完成，TXT 文件已生成: {output_file}")
