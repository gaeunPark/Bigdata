# coding: cp949

num=1
sum=0
while True:
    # ī����
    num=str(num)
    sum += num.count("8")
    
    num=int(num)
    num +=1
    
    # ����
    if num>100000:
        break

print(sum)
