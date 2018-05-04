# coding: cp949
info = """
< Menu >
1. 커피구매
2. 커피잔량 확인
3. 프로그램 종료

메뉴를 선택하세요: """

coffee_number = 10
while True:
    select = int(input(info))

    if select == 1:
        money = int(input("금액을 입력하세요: "))
        if money == 300:
            print("커피를 줍니다.")
            coffee_number = coffee_number -1
        elif money < 300 and money >0:
            print("금액이 %d 모자랍니다." %(300-money))
        elif money > 300:
            print("커피를 줍니다. 거스름 돈 %d입니다." %(money-300))
            coffee_number = coffee_number -1
        
        if not coffee_number:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break

    elif select == 2:
        print("남은 커피의 양은 %d입니다." %coffee_number)
   
    elif select == 3:
        print("프로그램을 종료합니다.")
        break

    else:
        print("다시 입력하세요.")
