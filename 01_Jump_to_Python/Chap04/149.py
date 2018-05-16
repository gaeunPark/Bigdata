def sum_and_num(a,b):
    return a+b, a*b

result = sum_and_num(3,4)
print(result)

sum, mul = sum_and_num(3,4)
print("%d %d" %(sum, mul))