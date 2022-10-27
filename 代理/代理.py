import parsel
import random
import requests
from openpyxl import Workbook
import time
from fake_useragent import UserAgent

# 随机UA
ua = UserAgent()

ajk_headers = {
    'User-Agent': ua.random,
}

ajk_list_url = 'https://www.baidu.com'

response = requests.get(ajk_list_url, headers=ajk_headers, proxies={"http": "http://127.0.0.1:24000"})
