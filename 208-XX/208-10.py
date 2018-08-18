import re
import requests
from html.parser import HTMLParser

url = "https://www.cwb.gov.tw/m/f/taiwan/36/63.htm"

code = requests.get(url)
code.encoding = "UTF-8"  # 設定編碼
html = code.text  # 讀出網頁全文


class MyParser(HTMLParser):
    result = ""

    def error(self, message):
        pass

    def handle_data(self, data):
        self.result += data


parser = MyParser()
parser.feed(html)
rows = parser.result.splitlines()
rows = map(lambda row: row.strip(), rows)
text = filter(lambda row: re.match("\S+", row), rows)

for t in list(text)[0:10]: # [0:10]只取第一天
    print(t)

input("Enter to exit")