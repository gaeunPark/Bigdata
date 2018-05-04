
num = 1000
sum =0
multy_3=0
multy_5=0
multy_15=0

while True:
    
    multy_3 +=3
    multy_5 +=5
    multy_15 +=15

    if multy_3<num:
        sum += multy_3

    if multy_5<num:
        sum += multy_5
    
    if multy_15<num:
        sum -= multy_15

    if multy_3>=num and multy_5>=num:
        break

print(sum)
    
        




