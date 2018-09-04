import pandas as pd

df = pd.read_csv("208-15.csv", encoding="UTF-8")

print("行業筆數為:", df.shape[0])  # shape回傳tuple(rows,cols)
for i in range(2, 16, 2):
    rawSeries = df.iloc[:, i]  # 將第i個col轉為Series物件
    numSeries = pd.to_numeric(rawSeries, errors='coerce')  # 將Series內的資料轉為數字，errors='coerce'轉換失敗以NaN取代
    print(f"{numSeries.name}的平均值為: %.2f" % (numSeries.mean(skipna=True)))

input("Enter to exit")
