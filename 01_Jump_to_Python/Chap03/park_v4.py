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
    
    # ��� ����
    print("------------------------------------")
    if fee != 0:
        money_type = int(input("��� ������ �����ϼ���.(1: ����, 2: ���� ���� �ſ�ī��): "))
        if money_type == 1:
            money = int(input("����� �Է��ϼ���: "))
            if money == fee:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif money < fee:
                print("[ %d ]�� ���ڶ��ϴ�. �Է��Ͻ� [ %d ]�� ��ȯ�մϴ�." %((fee-money), money))
            elif money > fee:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� [ %d ]�� ��ȯ�մϴ�." %(money-fee))
        elif money_type == 2:
            if age>=60 and age<=65: 
                fee = (fee*0.9)*0.95
            else:
                fee = (fee*0.9)
            print("[ %d ]�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %fee)







