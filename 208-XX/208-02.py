h=float(input("請輸入身高, 單位為公分: "))
w=float(input("請輸入體重, 單位為公斤: "))
bmi=w/(h/100)**2

if bmi<18.5 :
    s="太輕"
elif 18.5<=bmi<25:
    s="正常"
elif 25<=bmi<=30:
    s="過重"
else :
    s="肥胖"

print("您的BMI為%7.3f"%(bmi)+", 您的體重"+s)