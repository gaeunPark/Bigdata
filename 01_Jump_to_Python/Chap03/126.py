# coding: cp949

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.\n")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다.\n" %(money-300))
        coffee = coffee -1
    else:
        print("돈을 다시 주고 커피를 주지 않습니다.")
        print("남은 커피 양은 %d입니다.\n" %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

