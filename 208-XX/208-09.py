import re, threading

pattern = r"^[\w+\-*\.?]+\w+@[\w+\.?]+\.[a-z]+$"


class matchFile(threading.Thread):
    def run(self):
        try:
            with open("208-09.txt", "r", encoding="UTF-8") as f:
                # 移除後綴 "\n" 可使用 .read() 讀取全檔再 .splitlines()
                # 保留後綴 "\n" 可使用 .readlines()
                rows = f.read().splitlines()
                f.close()
        except IOError:
            print("Source File Error")

        # additional example for pattern match test
        # rows.append("te_s-T.num__-123@re01.matchesmail.net")

        emails = filter(lambda row: re.match(pattern, row), rows)
        mi.join()  # 等使用者輸入完畢再列印
        print("====== 檔案內有效email address如下 ======")
        for mail in emails:
            print(mail)


class matchInput(threading.Thread):
    def run(self):
        text = "User input email for test"
        users = []
        while text != "":
            text = input("請輸入要比對的email address(直接Enter結束): ")
            users.append(text)
        emails = filter(lambda row: re.match(pattern, row), users)
        print("====== 輸入的有效email address如下 ======")
        for mail in emails:
            print(mail)
        input("\nEnter to continue...")


mf = matchFile()
mi = matchInput()
mf.start()  # 先做檔案比對
mi.start()  # 出現提示輸入
mf.join()
input("\n====== 比對結束 ====== \n\nEnter to exit")
