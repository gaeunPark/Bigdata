
num_list = input("숫자를 입력하세요: ")

result = True
check = []
while(True):
    if len(num_list) != 10:
        result = False
        break

    for num in num_list:
        if num not in check:
            check.append(num)
        else:
            result = False
            break

    break

print(result)

