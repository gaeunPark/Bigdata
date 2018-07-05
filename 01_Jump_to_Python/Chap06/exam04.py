
while(True):
    age = input("나이를 입력하세요.(종료 입력시 종료): ")
    if age == '종료':
        break

    age = int(age)
    if age  < 3:
        fee = 0
    elif age < 13:
        fee = 10
    else:
        fee = 5

    print("요금은 %d입니다" %fee)

print("종료되었습니다.")