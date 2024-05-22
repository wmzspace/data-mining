import pandas as pd
import requests
from io import StringIO

# CSV文件的URL
csv_url = "https://healthdata.gov/resource/xkzp-zhs7.csv"

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
df.to_csv("COVID-19_Treatments_Cleaned.csv", index=False)

print("The CSV file was successfully downloaded, cleaned and saved.")
