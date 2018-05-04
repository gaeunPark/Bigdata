# coding: cp949

m = int(input("총 건수를 입력하세요: "))
n= int(input("한페이지에 보여줄 게시물 수: "))
if n<=0:
    print("다시 입력하세요")
else:
    if m==0:
        result=0
    else:
        result=(m//n)+1

print("%d   %d  %d" %(m, n, result))
