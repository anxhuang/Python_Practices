import urllib.request
import numpy as np

url = "http://opendataap2.penghu.gov.tw/resource/files/2018-08-01/5a57d0a9729568b778934dc37c4e3391.csv"
tmpFile = "208-13.csv"
urllib.request.urlretrieve(url, tmpFile)  # 下載檔案
rows = np.genfromtxt(tmpFile, dtype=int, delimiter=',', skip_header=1, encoding="UTF-8")  # 從檔案讀取numpy陣列

rows = rows[0:-5, (0, 1, 3, 4)]  # 用[0:-5,:]移除檔尾多餘部分, (0,1,3,4)是要留下來計算的欄位
rows[:, 2] += rows[:, 3]  # !!!重點!!! 將"欄3"加到"欄2"的寫法
rows = np.delete(rows, 3, axis=1)  # 移除多餘的欄3

for row in rows:
    print(f"{row[0]}年{row[1]}月 就讀國小(含)之前的人數:{row[2]}")

input("Enter to exit")