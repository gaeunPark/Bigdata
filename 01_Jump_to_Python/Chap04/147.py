# coding: cp949

def sum_many(*args):
    sum=0
    for i in args:
        sum = sum + i
    return sum

result = sum_many(1,2,3,4,5)
print(result)

def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
        return result
   
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
        return result

    elif choice == "sub":
        result = args[0]
        for i in args[1:]:
            result = result - i
        return result
   
    elif choice == "div":
        result = args[0]
        for i in args[1:]:
            result = result/i
        return result

sum_result = sum_mul("sum", 1,2,3,4,5)
mul_result = sum_mul("mul", 1,2,3,4,5)
sub_result = sum_mul("sub", 10,5,4,3,2)
div_result = sum_mul("div", 10,5,2)

print(sum_result)
print(mul_result)
print(sub_result)
print(div_result)
