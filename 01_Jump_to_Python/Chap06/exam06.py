def compare():
    while(True):
        num = int(input("양수를 입력하세요(종료:-1) : "))
        if num == -1:
            break

        if num % 10 == 0:
            result = True
        else:
            result = False
        print(result)


compare()
