
# f= open("연습생.txt", "w", encoding="UTF-8")
# for i in range(1, 5):
#    data=input() +"\n"
#    f.write(data)
# f.close()

def show_candidates(candidate_list):
    for i in candidate_list:
        print(i)

def make_idol(candidate_list):
    for i in candidate_list:
        print("신예 아이돌 %s 인기 급상승" %i)

def make_world_star(candidate_list):
    for i in candidate_list:
        print("아이돌 %s 월드스타 등극" %i)


f = open("연습생.txt", "r", encoding="utf-8")
candidate_list = []
while True:
    candidate = f.readline()
    if not candidate: break
    candidate=candidate[0:-1]
    candidate_list.append(candidate)

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)

f.close()