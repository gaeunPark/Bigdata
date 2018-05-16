def input_ingredient():
    ingredient_list = []
    while True:
        ingredient = input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if ingredient == "종료":
            break
        else:
            ingredient_list.append(ingredient)

    return ingredient_list

def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for ingredient in ingredient_list:
        print("%s 추가합니다." %ingredient)

    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.\n")
    print("-----------------------------------------")


menu = 0
ingredient_list=[]
while True:
    menu = int(input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n 1.주문\n 2.종료\n 입력: "))

    if menu == 2:
        break
    elif menu == 1:
        ingredient_list = input_ingredient()
    else:
        print("다시 입력하세요")
        continue

    make_sandwiches(ingredient_list)




