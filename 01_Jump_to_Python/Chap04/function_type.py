# coding: cp949
# �Է�: ����(Argument, Parameter)
# ���: return(print�� �ǹ��ϴ� ���� �ƴ�)

def my_sum1(num1, num2):    # �Է�, ����� ��� �����ϴ� ���̽�
    result = num1+num2;
    return result   # ����, ����Ͻ� �������� ����

def my_sum2(num1, num2):    # �Է¸� �ִ� ���̽�
    result = num1+num2;
    print("%d + %d = %d" %(num1, num2, result)) # ����� �ʿ���ų� ��� ó��

def my_sum3(num1, num2):    # ���(return)�� �ִ� ���̽�
    # �Է��� �Լ��ȿ��� ó��
    num1 = int(input("ù��° ���� �Է��ϼ���: "))
    num2 = int(input("�ι�° ���� �Է��ϼ���: "))
    result = num1+num2;
    return result

def my_sum4(num1, num2):    # �Է¸� �ִ� ���̽�
    # �Է��� �Լ��ȿ��� ó��
    num1 = int(input("ù��° ���� �Է��ϼ���: "))
    num2 = int(input("�ι�° ���� �Է��ϼ���: "))
    result = num1+num2;
    print("%d + %d = %d" %(num1, num2, result)) # ����� �ʿ���ų� ��� ó��

num1 = int(input("ù��° ���� �Է��ϼ���: "))
num2 = int(input("�ι�° ���� �Է��ϼ���: "))
result = my_sum1(num1, num2)
print("%d + %d = %d" %(num1, num2, result))

num1 = int(input("ù��° ���� �Է��ϼ���: "))
num2 = int(input("�ι�° ���� �Է��ϼ���: "))
my_sum(num1, num2)
result = my_sum3()
print("%d + %d = %d" %(num1, num2, result))
my_sum4()

def my_sum2_2():
    global num1
    num1 = num1+100
    result = num1+num2
    return result

num1 = int(input("ù��° ���� �Է��ϼ���: "))
num2 = int(input("�ι�° ���� �Է��ϼ���: "))
print("%d + %d = %d" %(num1, num2, result))



