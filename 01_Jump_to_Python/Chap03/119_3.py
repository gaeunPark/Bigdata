# coding: cp949
A = True
B= False

if A==False and B==False:
    print("A==False and B==False 조건이여야 수행되는 명령문")

if A and B == False:
    print("""A==False and B=False 조건이여야 수행하는 의도라면 
    현재 A는 False인데도 print가 되기 때문에 조건식이 잘못 작성되었음""")
