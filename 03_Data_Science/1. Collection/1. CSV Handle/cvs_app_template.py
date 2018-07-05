import csv
import math

def get_csv_row_instance(primary_key):
    row_instance = []
    row_index = 0
    NotFound = True
    for i in range(len(data)):
        if primary_key in data[i]:
            row_index = i
            NotFound = False
            break
        else:
            NotFound = True
    return  row_instance

def get_csv_col_instance(col_name):
    col_instance=[]
    col_index = data[0].index(col_name)
    for row in data[1:]:
        col_instance.append(row[col_index])

    col_instance = Convert_Type(col_instance)
    return col_instance

def Convert_Type(col_instance):
    try:
        col_instance = list(map(int, col_instance))
    except ValueError:
        col_instance = list(map(float, col_instance))
    return col_instance

def My_Sum(data_list):
    My_Sum = sum(data_list)
    return My_Sum

def My_Average(data_list):
    My_Average = My_Sum(data_list)/len(data_list)
    return My_Average

def My_Max(data_list):
    My_Max = max(data_list)
    return My_Max

def My_Min(data_list):
    My_Min = min(data_list)
    return My_Min

def My_Deviation(data_list):
    My_Deviation = []
    My_Deviation.append(data_list - My_Average(data_list))
    return(My_Deviation)

def My_Standard_Deviation(data_list):# 표준편차
    Variance=0


    return My_Standard_Deviation

def My_Variance(data_list):#분산
    My_Variance=0


    return My_Variance

def My_Ascendant(data_list):#오름차순
    # 내용을 작성하세요.
    pass

def My_Descendant(data_list):#내림차순
    # 내용을 작성하세요.
    pass

def print_row(row_instance):
    for row_element in row_instance:
        print("%s " %row_element,end="")
    print()
    pass

def print_col(col_instance):
    for col_element in col_instance:
        print(col_element)
    pass

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data=list(csv.reader(infile))


# menu 처리
while(True):
    print("0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬")
    menu = int(input("메뉴를 선택하세요: "))
    # key = input("Access Key를 입력하세요: ")
    key = 'COUNT PARTICIPANTS'
    if menu == 0:
        print("프로그램을 종료합니다.")
        break

    if menu == 1:
        print_row(get_csv_row_instance(key))

    elif menu == 2:
        print_col(get_csv_col_instance(key))

    elif menu == 3:
        data_list = get_csv_col_instance(key)
        print("총합: %d"  %My_Sum(data_list))

    elif menu == 4:
        data_list = get_csv_col_instance(key)
        print("평균: %d"  %My_Average(data_list))

    elif menu == 5:
        data_list = get_csv_col_instance(key)
        print("최대값: %d"  %My_Max(data_list))

    elif menu == 6:
        data_list = get_csv_col_instance(key)
        print("최소값: %d"  %My_Min(data_list))

    elif menu == 7:
        data_list = get_csv_col_instance(key)
        print("편차: %d"  %My_Deviation(data_list))

    elif menu == 8:
        data_list = get_csv_col_instance(key)
        print("표준편차: %d"  %My_Standard_Deviation(data_list))

    elif menu == 9:
        data_list = get_csv_col_instance(key)
        print("분산: %d"  %My_Variance(data_list))

    elif menu == 10:
        data_list = get_csv_col_instance(key)
        print("오름차순 정렬: %d"  %My_Sum(data_list))

    elif menu == 11:
        data_list = get_csv_col_instance(key)
        print("내림차순 정렬: %d"  %My_Sum(data_list))
















