# coding:cp949

print("������ ��� ���α׷� ver3.0")

while True:
    num=int(input("Ȧ���� �Է��ϼ���(0 <- ����): "))

    if num==0:
        break
    elif num%2==0:
        print("¦���� �Է��ϼ̽��ϴ�. ���Է��ϼ���")
        continue
    
    print(" ", end='')
    print("-"*num)

    i=0
    n=int((num+1)/2)
    while i < n:
        i += 1
        print("|", end='')
        print(" "*(n-i), end='')
        print("*"*(2*i-1), end='')
        print(" "*(n-i), end='')
        print("|")
    i=0
    while i < (n-1):
        i += 1
        print("|", end='')
        print(" "*i, end='')
        print("*"*(num-2*i), end='')
        print(" "*i, end='')
        print("|")
    
    print(" ", end='')
    print("-"*num)
