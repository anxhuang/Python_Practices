import requests
import bs4

url="https://www.cwb.gov.tw/m/f/taiwan/36/63.htm"

code = requests.get(url)
code.encoding = "UTF-8"
html = code.text

bs = bs4.BeautifulSoup(html, "lxml")
bs = bs.find("table", class_="table table-bordered table-36hr")
th = map(lambda tag: tag.get_text(), bs.find_all("th"))
td = map(lambda tag: tag.get_text(), bs.find_all("td"))
th = list(th)
td = list(td)

print(th)
print(td)
for i in range(0,4):
    print(th[i]+": "+td[i])

input("Enter to exit")