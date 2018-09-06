import pandas as pd

df = pd.read_csv("208-15.csv", encoding="UTF-8")

# 將所有紀錄內的'…'與'—'取代為0
df = df.replace(["…", "—"], 0)

# 刪除以下的columns
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

# 更改以下columns的index，原本的名稱:新的名稱
df = df.rename(columns={
    '經常性薪資-薪資': '經常性',
    '專業人員-薪資': '專業人員',
    '技術員及助理專業人員-薪資': '技術員及助理',
    '事務支援人員-薪資': '事務人員',
    '服務及銷售工作人員-薪資': '服務銷售',
    '技藝_機械設備操作及組裝人員-薪資': '機械設備操作',
    '基層技術工及勞力工-薪資': '基層勞力'
})

print(df)

input("Enter to exit")
