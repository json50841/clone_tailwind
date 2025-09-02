# backend/app/data_analy/dataanaly.py
from data_analy.datacatch import run_analysis


def run_analysis_wrapper():
    analysis_result = run_analysis()  # 调用 datacatch.py 的 run_analysis
    return {
        "status": "分析完成",
        "data": [1, 2, 3],
        **analysis_result,  # 将 analysis_result 的键值对展开到最外层
    }
