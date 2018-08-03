total=0
book={}
while True:
    item=input("消費項目: ")
    price=int(input("消費金額: "))
    if (total+price)<=1000:
        total+=price
        book[item]=price
        print(f"目前消費金額: {total}")
    else:
        print("已經超支了\n",book)
        break
input("Enter to exit")