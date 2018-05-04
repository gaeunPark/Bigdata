# coding: cp949

array = [-1, 1, 3, -2, 2]
negative =0

# 음수 갯수
for i in array:
    if i<0:
        negative +=1

# 재배열
answer=array[:]
len=len(array)
ne_idx=0
po_idx=negative

for i in range(len):
    if array[i]<0:
        answer[ne_idx]=array[i]
        ne_idx += 1
    elif array[i]>=0:
        answer[po_idx]=array[i]
        po_idx += 1

print(answer)
        






