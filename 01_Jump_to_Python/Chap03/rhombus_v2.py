# coding:cp949

print("마름모 출력 프로그램 ver2.0")

while True:
    num=int(input("홀수를 입력하세요(0 <- 종료): "))

    if num==0:
        break
    elif num%2==0:
        print("짝수를 입력하셨습니다. 재입력하세요")
        continue
    
    i=0
    n=int((num+1)/2)
    while i < n:
        i += 1
        print(" "*(n-i), end='')
        print("*"*(2*i-1))
    i=0
    while i < (n-1):
        i += 1
        print(" "*i, end='')
        print("*"*(num-2*i))

