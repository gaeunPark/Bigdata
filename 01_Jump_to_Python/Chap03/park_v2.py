#coding: cp949

fee = 0
age = int(input("���̸� �Է��ϼ���: "))
if age < 0:
    print("�ٽ� �Է��ϼ���")
else:
    if age>=0 and age<=3:
        fee = 0
        grade = "����"
    elif age>=4 and age<=13:
        fee = 2000
        grade = "���"
    elif age>=14 and age<=18:
        fee = 3000
        grade = "û�ҳ�"
    elif age>=19 and age<=65:
        fee = 5000
        grade = "����"
    else:
        fee = 0
        grade = "����"
    print("���ϴ� [ %s ]����̸� ����� [ %d ]�� �Դϴ�." %(grade, fee))
        







