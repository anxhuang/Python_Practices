print("五次失敗就會退出遊戲")
chain=""
while chain == "":
    chain=input("請輸入一個字串: ")
text = input("上一個字串是 %s"%(chain)+"\n請輸入-" + chain[-1] + "-開始的字串: ")
fail=1
while fail < 5:
    if text != "" and text[0] == chain[-1]:
        chain += "-" + text
        text = input("上一個字串是 %s"%(chain)+"\n請輸入-" + chain[-1] + "-開始的字串: ")
    else:
        text = input("輸入失敗" + str(fail) + "次, 請再次輸入-" + chain[-1] + "-開始的字串: ")
        fail += 1
print("輸入失敗" + str(fail) + "次, 遊戲結束...")