# coding: cp949
info = """
< Menu >
1. Ŀ�Ǳ���
2. Ŀ���ܷ� Ȯ��
3. ���α׷� ����

�޴��� �����ϼ���: """

coffee_number = 10
while True:
    select = int(input(info))

    if select == 1:
        money = int(input("�ݾ��� �Է��ϼ���: "))
        if money == 300:
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee_number = coffee_number -1
        elif money < 300 and money >0:
            print("�ݾ��� %d ���ڶ��ϴ�." %(300-money))
        elif money > 300:
            print("Ŀ�Ǹ� �ݴϴ�. �Ž��� �� %d�Դϴ�." %(money-300))
            coffee_number = coffee_number -1
        
        if not coffee_number:
            print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
            break

    elif select == 2:
        print("���� Ŀ���� ���� %d�Դϴ�." %coffee_number)
   
    elif select == 3:
        print("���α׷��� �����մϴ�.")
        break

    else:
        print("�ٽ� �Է��ϼ���.")
