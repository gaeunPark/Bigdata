#coding: cp949

fee = 0
age = int(input("나이를 입력하세요: "))
if age < 0:
    print("다시 입력하세요")
else:
    if age>=0 and age<=3:
        fee = 0
        grade = "유아"
    elif age>=4 and age<=13:
        fee = 2000
        grade = "어린이"
    elif age>=14 and age<=18:
        fee = 3000
        grade = "청소년"
    elif age>=19 and age<=65:
        fee = 5000
        grade = "성인"
    else:
        fee = 0
        grade = "노인"
    print("귀하는 [ %s ]등급이며 요금은 [ %d ]원 입니다." %(grade, fee))
    
    # 요금 유형
    print("------------------------------------")
    if fee != 0:
        money_type = int(input("요금 유형을 선택하세요.(1: 현금, 2: 공원 전용 신용카드): "))
        if money_type == 1:
            money = int(input("요금을 입력하세요: "))
            if money == fee:
                print("감사합니다. 티켓을 발행합니다.")
            elif money < fee:
                print("[ %d ]가 모자랍니다. 입력하신 [ %d ]를 반환합니다." %((fee-money), money))
            elif money > fee:
                print("감사합니다. 티켓을 발행하고 거스름돈 [ %d ]를 반환합니다." %(money-fee))
        elif money_type == 2:
            if age>=60 and age<=65: 
                fee = (fee*0.9)*0.95
            else:
                fee = (fee*0.9)
            print("[ %d ]원 결제 되었습니다. 티켓을 발행합니다." %fee)







