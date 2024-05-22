import re

import requests
from bs4 import BeautifulSoup

import clean_data

# 要解析的网页URL
url = "https://healthdata.gov/ASPR/COVID-19-Treatments/xkzp-zhs7/about_data"

# 发送请求以获取网页内容
response = requests.get(url)
response.raise_for_status()  # 检查请求是否成功

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.content, "html.parser")

# 正则表达式查找所有符合条件的链接
csv_links = re.findall(r'https://healthdata.gov/resource/[a-zA-Z0-9_-]+\.csv', str(soup))

# 打印找到的所有CSV链接
for link in csv_links:
    print("csv link found: " + link)
    clean_data.get_data(link)
