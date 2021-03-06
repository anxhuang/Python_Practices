# ====== 特別說明: 208-18為接續208-17 ==============
import pandas as pd

df = pd.read_csv("208-15.csv", encoding="UTF-8")

# 1. 將所有紀錄內的'…'與'—'取代為0
df = df.replace(["…", "—"], 0)

# 2. 刪除以下的columns
df = df.drop(columns=[
    '年度',
    '經常性薪資-女/男',
    '專業人員-女/男',
    '技術員及助理專業人員-女/男',
    '事務支援人員-女/男',
    '服務及銷售工作人員-女/男',
    '技藝_機械設備操作及組裝人員-女/男',
    '基層技術工及勞力工-女/男'
])

# 3. 更改以下columns的index，原本的名稱:新的名稱
df = df.rename(columns={
    '經常性薪資-薪資': '經常性',
    '專業人員-薪資': '專業人員',
    '技術員及助理專業人員-薪資': '技術員及助理',
    '事務支援人員-薪資': '事務人員',
    '服務及銷售工作人員-薪資': '服務銷售',
    '技藝_機械設備操作及組裝人員-薪資': '機械設備操作',
    '基層技術工及勞力工-薪資': '基層勞力'
})

# ====== 以上為208-17之操作，以下為208-18之操作 ======

# 1. Columns的格式設定為int
df = df.drop(columns='行業別')
df = df.astype(dtype=int)

# 2.計算'經常性'、'專業人員'、'技術員及助理'與'事務人員'的薪資中位數、平均數、最大值、最小值
dfa = df.agg(["median", "mean", "max", "min"])  # agg可直接由字串調用方法
pd.options.display.float_format = "{:.2f}".format  # 設定數字格式的屬性
print(dfa.iloc[:, 0:4])

# 3.計算'服務銷售','機械設備操作'與'基層勞力'的薪資中位數、平均數、最大值、最小值
print(dfa.iloc[:, 4:])

input("Enter to exit")
