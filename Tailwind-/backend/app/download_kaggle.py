import os
import json
import stat
import subprocess

# 1. kaggle.json 内容
kaggle_token = {
    "username": "uoihkhkujkjnknjk",
    "key": "4b7ba015f98f36e011dfab7c62ad7a88"
}

# 2. 创建 .kaggle 目录
kaggle_dir = os.path.expanduser("~/.kaggle")
os.makedirs(kaggle_dir, exist_ok=True)

# 3. 写入 kaggle.json
kaggle_json_path = os.path.join(kaggle_dir, "kaggle.json")
with open(kaggle_json_path, "w") as f:
    json.dump(kaggle_token, f)

# 4. 设置权限为 600
os.chmod(kaggle_json_path, stat.S_IRUSR | stat.S_IWUSR)

print(f"Created kaggle.json at {kaggle_json_path}")

# 5. 安装 kaggle 包（如果没安装）
try:
    import kaggle
except ImportError:
    print("kaggle package not found, installing...")
    subprocess.check_call(["pip", "install", "kaggle"])

# 6. 下载 Titanic 竞赛数据集示例
print("Downloading Titanic dataset...")
subprocess.check_call(["kaggle", "competitions", "download", "-c", "titanic"])

# 7. 解压下载的 zip 文件
import zipfile

zip_path = "titanic.zip"
extract_dir = "titanic_data"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_dir)

print(f"Extracted Titanic dataset to folder '{extract_dir}'")
