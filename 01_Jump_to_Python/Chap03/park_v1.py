#coding: cp949

fee = 0
age = int(input("나이를 입력하세요: "))
    
if age>=0 and age<=3:
     fee = 0
elif age>=4 and age<=13:
    fee = 2000
elif age>=14 and age<=18:
    fee = 3000
elif age>=19 and age<=65:
    fee = 5000
else:
    fee = 0

print("요금은 [%d]원 입니다." %fee)








