import os
import pandas as pd
import kagglehub


def run_analysis():
    """
    下载 Kaggle 数据集，并返回字典格式结果（可直接序列化为 JSON）
    """
    try:
        # 下载最新版本数据集，返回本地路径
        dataset_path = kagglehub.dataset_download(
            "abdullah0a/retail-sales-data-with-seasonal-trends-and-marketing"
        )

        # 自动找到 CSV 文件
        csv_files = [f for f in os.listdir(dataset_path) if f.endswith(".csv")]
        if not csv_files:
            return {"status": "分析失败", "error": "数据集中没有 CSV 文件"}

        # 读取第一个 CSV 文件
        df = pd.read_csv(os.path.join(dataset_path, csv_files[0]))

        return {
            "status": "分析完成",
            "data2": df.head(5).to_dict(orient="records"),  # 前5行示例
        }

    except Exception as e:
        return {"status": "分析失败", "error": str(e)}


# 测试
if __name__ == "__main__":
    print(run_analysis())
