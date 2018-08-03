print("請輸入字串，當您輸入0就代表結束")
allText=[]
okText=[]
while True:
    text = input("請輸入:")
    if text == "0":
        break
    elif text == text[::-1]: #重點: 用string[::-1] 代表將字串反轉
        okText.append(text)
    allText.append(text)
print(f"顯示清單內容:\n{allText}\n符合回文的字串為:\n{okText}") #f-string: f"insert a {var} in string" (Python 3.6 up)
input("Enter to exit")