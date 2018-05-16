class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self, other):
        print("저희 레스토랑 명칭은 [ %s ]이고 [ %s ] 전문점입니다." %(self.restaurant_name, other.cuisine_type))

    def open_restaurant(self):
        print("저희 [ %s ] 레스토랑 오픈했습니다. 어서오세요\n" %self.restaurant_name)

    def reset_number_served(self, number):
        print("손님 카운팅을 %d으로 초기화 하였습니다.\n" %number)
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다.\n" %self.number_served)

    def __del__(self):
        print("%s 레스토랑 문 닫습니다." %self.restaurant_name)

class Korean_Rest(Restaurant):
    cuisine_type = "한식"
    def __init__(self):
        self.cuisine_type = "한식"

    def order_menu(self):
        print("한식을 주문합니다.")

class Japanes_Rest(Restaurant):
    cuisine_type = "일식"
    def order_menu(self):
        print("일식을 주문합니다.")

data = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분, 1:한식 2:일식): ")
data = data.split()
restaurant = Restaurant(data[0], data[1])
korean = Korean_Rest(data[0], "한식")
japan = Japanes_Rest(data[0], "일식")

if data[1] == "1":
    restaurant+korean
elif data[1] == "2":
    restaurant+japan

restaurant.describe_restaurant()
open = input("레스토랑을 오픈하시겠습니까?(y/n): \n" )
if open == "y":
    restaurant.open_restaurant()

while True:
    if open == "n":
        break
    number = input("어서오세요. 몇명이십니까?(초기화:0, 종료:-1, 누적고객 확인:p : ")
    if number == "0":
        restaurant.reset_number_served(int(number))
    elif number == "-1":
        break
    elif number == "p":
        restaurant.check_customer_number()
    else:
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다.\n" %number)
        restaurant.increment_number_served(int(number))