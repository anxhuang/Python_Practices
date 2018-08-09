import csv, json

zipCode = ""
while zipCode == "":
    zipCode = input("請輸入郵遞區號: ")

# read from csv
try:
    f = open("208-08.csv", "r", encoding="UTF-8")
    rows = csv.reader(f)
    for row in rows:
        if row[2] == zipCode:
            print(f"csv: {row}")
    f.close()
except FileNotFoundError:
    print("CSV File Not Found")
except PermissionError:
    print("CSV File Permission Error")
except IOError:
    print("File I/O Error")

# read from json
try:
    with open("208-08.json", "r", encoding="UTF-8") as f:  # 用with...as會自動f.close()
        rows = json.load(f)
        for row in rows:
            if row['郵遞區號'] == zipCode:
                print("json: "+str(list(row.values())))
except FileNotFoundError:
    print("JSON File Not Found")
except PermissionError:
    print("JSON File Permission Error")
except IOError:
    print("File I/O Error")

input("Enter to exit")


