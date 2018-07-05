
while(True):
    num1, num2, num3 = map(lambda convert_num: int(convert_num), input("세 개의 양수를 입력하세요(종료 -1): ").split(" "))

    # if int(num1) != -1:
    #     num1 = int(num1)
    #     num2 = int(num2)
    #     num3 = int(num3)

    if num3 % (num1*num2) == 0:
        print("%d는 %d와 %d의 공배수 입니다." %(num1, num2, num3))
    else:
        print("%d는 %d와 %d의 공배수가 아닙니다." % (num1, num2, num3))

