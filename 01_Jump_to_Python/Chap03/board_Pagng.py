# coding: cp949

m = int(input("�� �Ǽ��� �Է��ϼ���: "))
n= int(input("���������� ������ �Խù� ��: "))
if n<=0:
    print("�ٽ� �Է��ϼ���")
else:
    if m==0:
        result=0
    else:
        result=(m//n)+1

print("%d   %d  %d" %(m, n, result))
