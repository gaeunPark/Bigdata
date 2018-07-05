import csv

def Convert_Type(col_instance):
    try:
        col_instance = list(map(int, col_instance))
    except ValueError:
        col_instance = list(map(float, col_instance))
    return col_instance

def print_row(row_instance):
    for row_element in row_instance:
        print("%s " %row_element,end="")
    print()

def print_col(col_instance):
    for col_element in col_instance:
        print(col_element)

with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as infile:
    data = list(csv.reader(infile))

print_row(data[1])
print_col(data[1])
print_col()

# while(True):
#     print("0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬")
#     menu = int(input("메뉴를 선택하세요: "))