# coding: cp949

num=10000
result=[]
muliple=0
while True:
    muliple += 63
    
    if muliple>num:
        break

    result.append(muliple)

print(result)
print("��� ��: %d" %len(result))



