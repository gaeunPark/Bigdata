# coding:cp949

print("������ ��� ���α׷� ver1.0")

while True:
    num=int(input("�غ� Ȧ���� �Է��ϼ���(0 <- ����): "))
   
    if num==0:
        break
    elif num%2==0:
        print("¦���� �Է��ϼ̽��ϴ�. ���Է��ϼ���")
        continue

    raw=int((num+1)/2)
    i=0
    while i < raw:
        i += 1
        print(" "*(raw-i), end='')
        print("*"*(2*i-1))
i
