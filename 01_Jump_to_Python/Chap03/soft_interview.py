# coding: cp949

name="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

name=name.split(",")

# 이름 성
family=[]
for i in name:
    family.append(i[0])
kim=family.count("김")
lee=family.count("이")
print("김씨: %d명, 이씨: %d명" %(kim, lee))

# 이재영 이름 수
q2=name.count("이재영")
print("이제영의 수: %d" %q2)

# 중복 제거 이름
name=set(name)
name=list(name)
print(name)

# 오름차순
name.sort()
print(name)



