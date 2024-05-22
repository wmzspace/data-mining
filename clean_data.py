import os
from io import StringIO

import pandas as pd
import requests


def get_data(csv_url):
    # 下载CSV文件内容
    response = requests.get(csv_url)
    response.raise_for_status()  # 检查请求是否成功

    # 将CSV内容读入DataFrame
    df = pd.read_csv(StringIO(response.text))

    # 基本预处理
    # 移除列名中的前后空白
    df.columns = df.columns.str.strip()

    # 将所有文本转换为小写（如果适用）
    df = df.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)

    # 显示清理后的DataFrame的前几行
    print(df.head())

    # 将清理后的DataFrame保存为新的CSV文件
    filename = os.path.basename(csv_url)
    df.to_csv(filename, index=False)

    print("The CSV file was successfully downloaded, cleaned and saved.")
