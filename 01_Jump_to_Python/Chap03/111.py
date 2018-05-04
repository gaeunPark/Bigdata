# coding: cp949

money=1
if money:
    print("택시를 타고 가라")
#  print("도착했습니다.")   <-indentation이 맞지 않아 에러
#    print("도착했습니다.") <- 동일한 코드가 중복이 됨
else:
    print("걸어 가라")
#  print("도착했습니다.")
#    print("도착했습니다.") <- 프로그램 수정시 동일한 코드 로직 변경이 누락될 가능성이 있음
print("목적지에 도착했습니다.")
print("프로그램 종료합니다.")
