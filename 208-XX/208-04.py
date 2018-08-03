fruits=["蘋果","西瓜","芒果","葡萄","橘子"]
while True:
    x = input("請輸入喜歡的水果(Enter 結束):")
    if x in fruits:
        print(x, " 在list清單中的第%d"%(fruits.index(x)+1)+"項")
    else:
        if x=="":
            break
        print(x, " 不在list清單中!")
input("Enter to exit")