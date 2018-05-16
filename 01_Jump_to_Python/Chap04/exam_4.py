
# f = open("방명록.txt", "w", encoding='utf-8')
# f.write("임꺽정 900327\n")
# f.write("홍길동 871021\n")

def search_visitor(visitor):
    f = open("방명록.txt", "r", encoding='utf-8')

    while True:
        line = f.readline()
        line = line.split()
        if not line: break
        name = line[0]

        if visitor == name:
            print("%s님 다시 방문해 주셔서 감사합니다. " %visitor)
            check = 0
            break
        else:
            check = 1

    f = open("방명록.txt", "a", encoding='utf-8')
    if check == 1:
        birth = input("생년월일을 입력하세요(예:801212): ")
        line = "%s %s\n" % (visitor, birth)
        f.write(line)
        print("%s님 환영합니다. 아래 내용을 입력하셨습니다." % visitor)
        print(line)


visitor = input("이름을 입력하세요: ")
search_visitor(visitor)



