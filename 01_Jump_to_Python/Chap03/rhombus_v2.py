# coding:cp949

print("������ ��� ���α׷� ver2.0")

while True:
    num=int(input("Ȧ���� �Է��ϼ���(0 <- ����): "))

    if num==0:
        break
    elif num%2==0:
        print("¦���� �Է��ϼ̽��ϴ�. ���Է��ϼ���")
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

