
count = 0
while(True):
    name = input("안녕하세요. 이름을 입력하세요(종료 입력시 종료): ")
    if name == "종료":
        break
    count += 1

    if count == 1:
        print("Hi [%s]!! You are %sst person come here!" %(name, count))
    elif count == 2:
        print("Hi [%s]!! You are %snd person come here!" % (name, count))
    elif count == 3:
        print("Hi [%s]!! You are %srd person come here!" % (name, count))
    elif count <= 10:
        print("Hi [%s]!! You are %sth person come here!" % (name, count))
    else:
        print("Sorry, [%s]!! The event is closed because You are %sth person come here" % (name, count))