# coding:cp949

print("마름모 출력 프로그램 ver1.0")

while True:
    num=int(input("밑변 홀수를 입력하세요(0 <- 종료): "))
   
    if num==0:
        break
    elif num%2==0:
        print("짝수를 입력하셨습니다. 재입력하세요")
        continue

    raw=int((num+1)/2)
    i=0
    while i < raw:
        i += 1
        print(" "*(raw-i), end='')
        print("*"*(2*i-1))
i
