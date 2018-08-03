n=int(input("請輸入幾個月: "))
passbook={} #dictionary
total=0
for i in range(n):
    cost=int(input("請輸入第%d個月的支出金額: "%(i+1)))
    passbook.update({i+1:cost})
    total+=cost

#用key=dict.get指定key需依照value排列
sortKey=sorted(passbook, key=passbook.get)
sortValue=sorted(passbook.values())
print("支出最多的金額為",sortKey[-1],"月:",sortValue[-1]) # 金額或用max(dict.values())
print("支出最少的金額為",sortKey[0],"月:",sortValue[0]) # 金額或用min(dict.values())
print("支出的總額為",total) # 總額或用sum(dict.values())
print("支出金額由小到大為:",sortValue)

#亦可以輸出為tuple指定給一個新的list接收
sortPassbook=[(k,passbook[k]) for k in sorted(passbook, key=passbook.get)]
print("支出最多的金額為",sortPassbook[-1][0],"月:",sortPassbook[-1][1])
print("支出最少的金額為",sortPassbook[0][0],"月:",sortPassbook[0][1])
print("支出的總額為",sum(passbook.values()))
print("支出金額由小到大為:",sorted(passbook.values()))

input("Enter to exit")