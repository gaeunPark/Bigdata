# coding: cp949

name="������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������"

name=name.split(",")

# �̸� ��
family=[]
for i in name:
    family.append(i[0])
kim=family.count("��")
lee=family.count("��")
print("�达: %d��, �̾�: %d��" %(kim, lee))

# ���翵 �̸� ��
q2=name.count("���翵")
print("�������� ��: %d" %q2)

# �ߺ� ���� �̸�
name=set(name)
name=list(name)
print(name)

# ��������
name.sort()
print(name)



