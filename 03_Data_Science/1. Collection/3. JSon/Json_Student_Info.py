import json

with open('ITT_Student.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)

f = open('D:/Python_Workspace/03_Data_Science/1. Collection/3. JSon/ITT_student_ID.txt', 'r', encoding='utf-8')
idxes = f.readlines()
idx = idxes[-1]
f.close()
# print(idx[:3] + str(int(idx[3:])+1))
def save():
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print('ITT_Student.json SAVED\n')
def print_menu():
    menu = int(input("""
*********************************************************************
<<JSON기반 관리 학생 정보 관리 프로그램>>>
    1. 학생 정보입력
    2. 학생 정보조회
    3. 학생 정보수정
    4. 학생 정보삭제
    5. 프로그램 종료
    메뉴를 선택하세요: """))
    print()
    return menu
def print_menu2():
    type = int(input("""1. 전체 학생정보 조회 
     검색 조건 선택
    2. ID 검색
    3. 이름 검색
    4. 나이 검색
    5. 주소 검색
    6. 과거 수강 횟수 검색
    7. 현재 강의를 수강중인 학생
    8. 현재 수강 중인 강의명
    9. 현재 수강 강사
    10. 이전 메뉴
    메뉴를 선택하세요: """))
    print()
    return type
def print_menu3():
    type = int(input("""1.학생 이름 
2. 나이
3. 주소
4. 과거 수강 횟수
5. 현재 수강 중인 강의 정보 
0. 이전 메뉴
메뉴를 선택하세요: """))
    print()
    return type
def print_menu3_5():
    type2 = int(input("""1.강의 코드 
2. 강의명
3. 강사
4. 개강일
5. 종료일
0. 취소
메뉴를 선택하세요: """))
    print()
    return type2
def print_menu4():
    type = int(input("""삭제 유형을 선택하세요. 
    1. 전체 삭제
    2. 현재 수강 중인 특정 과목정보 삭제
    3. 이전 메뉴 
    메뉴를 선택하세요: """))
    print()
    return type

def Input_Student_Info():
    student_ID = 'ITT007' #idx[:3] + int(idx[3:])+1
    Student_info_list = []
    json_big_data.append(
    {
        "address": input('주소 (예: 대구광역시 동구 아양로 135): '),
        "student_ID": student_ID,
        "student_age": input('나이 (예: 29): '),
        "student_name": input('이름 (예: 홍길동): '),
        "total_course_info": {
            "learning_course_info": Input_Couse_Info(),
            "num_of_course_learned": input('과거 수강 횟수 (예: 1): ')
        }
    }
    )
    save()

def Input_Couse_Info():
    learning_course_info = []
    while True:
        check = input('현재 수강 과목이 있습니까? (에: y/n): ')
        if check == 'n': break
        else:
            learning_course_info.append(
            {
                "close_date": input('종료일 (예: 2018-09-05): '),
                "course_code": input('강의코드 (예: IB171106, OB0104..): '),
                "course_name": input('강의명 (예: IOT빅데이터 실무반): '),
                "open_date": input('개강일 (예: 2017-11-06): '),
                "teacher": input('강사 (예: 이현구): '),
            }
            )
    return learning_course_info

def Total_Search():
    for Student in json_big_data:
        print("""* 학생 ID: %s 
* 이름: %s
* 나이: %s
* 주소: %s
* 수강 정보
 + 과거 수강 횟수: %s""" %( Student['student_ID'], Student['student_name'], Student['student_age'], Student['address'], Student['total_course_info']['num_of_course_learned']))
        for course in Student['total_course_info']['learning_course_info']:
            print(""" + 현재 수강 과목
    강의 코드: %s
    강의명: %s
    강사: %s
    개강일: %s
    종료일: %s""" %(course['course_code'], course['course_name'], course['teacher'], course['open_date'], course['close_date']))
        print()

def Search_ID(student_ID):
    for Student in json_big_data:
        if Student['student_ID'] == student_ID:
            print("""* 학생 ID: %s 
* 이름: %s
* 나이: %s
* 주소: %s
* 수강 정보
+ 과거 수강 횟수: %s""" % (Student['student_ID'], Student['student_name'], Student['student_age'], Student['address'], Student['total_course_info']['num_of_course_learned']))
            for course in Student['total_course_info']['learning_course_info']:
                print(""" + 현재 수강 과목
    강의 코드: %s
    강의명: %s
    강사: %s
    개강일: %s
    종료일: %s""" % (course['course_code'], course['course_name'], course['teacher'], course['open_date'], course['close_date']))
            print()

def Search_multipleID(student_ID):
    for Student in json_big_data:
        if Student['student_ID'] == student_ID:
            print("""* 학생 ID: %s 
* 학생 이름: %s
""" % (Student['student_ID'], Student['student_name']))

def Search(type, find_key):
    if type == 2: type_name = 'student_ID'
    elif type == 3: type_name = 'student_name'
    elif type == 4: type_name = 'student_age'
    elif type == 5: type_name  = 'address'
    elif type == 6: type_name = 'num_of_course_learned'
    elif type == 7: type_name = 'total_course_info'
    elif type == 8: type_name = 'course_name'
    elif type == 9: type_name = 'teacher'

    student_ID = []

    for Student in json_big_data:
        if type>=2 and type<=5:
            if Student[type_name].find(find_key) != -1:
                student_ID.append(Student['student_ID'])
        elif type == 6:
            if Student['total_course_info'][type_name].find(find_key) != -1:
                student_ID.append(Student['student_ID'])
        elif type == 7:
            if len(Student[type_name]['learning_course_info']) != 0:
                student_ID.append(Student['student_ID'])

        for course in Student['total_course_info']['learning_course_info']:
            if type>=8:
                if course[type_name].find(find_key) != -1:
                    student_ID.append(Student['student_ID'])

    student_ID = set(student_ID)

    for ID in student_ID:
        if len(student_ID) == 1:
            Search_ID(ID)
        elif len(student_ID) >= 2:
            Search_multipleID(ID)
        elif len(student_ID) == 0:
            print("찾는값이 없습니다.")

def delete(student_ID):
    for i in range(len(json_big_data)):
        if json_big_data[i]['student_ID'] == student_ID:
            del json_big_data[i]
    save()

def delete_course(student_ID):
    for i in range(len(json_big_data)):
        if json_big_data[i]['student_ID'] == student_ID:
            print("수강중인 강의코드 입니다.")
            for course in json_big_data[i]['total_course_info']['learning_course_info']:
                print(course['course_code'])

            code = input("삭제할 강의 코드를 입력하십시오: ")
            for j in range(len(json_big_data[i]['total_course_info']['learning_course_info'])):
                # tt = json_big_data[i]['total_course_info']['learning_course_info'][j]['course_code']
                if json_big_data[i]['total_course_info']['learning_course_info'][j]['course_code'] == code:
                    del (json_big_data[i]['total_course_info']['learning_course_info'])[j]
    save()

def alert(type, student_ID):
    change = input("변경할 값을 입력하세요: ")
    if type == 1: type_name = 'student_name'
    elif type == 2: type_name = 'student_age'
    elif type == 3: type_name  = 'address'
    elif type == 4: type_name = 'num_of_course_learned'

    for i in range(len(json_big_data)):
        if json_big_data[i]['student_ID'] == student_ID:
            if type >=1 and type <=3:
                json_big_data[i][type_name] = change
            elif type == 4:
                json_big_data[i]['total_course_info'][type_name] == change
    save()

def alert_course(type, student_ID):
    change = input("변경할 값을 입력하세요: ")
    if type == 1: type_name = 'course_code'
    elif type == 2: type_name = 'course_name'
    elif type == 3: type_name  = 'teacher'
    elif type == 4: type_name = 'open_date'
    elif type == 5: type_name = 'close_date'

    for i in range(len(json_big_data)):
        if json_big_data[i]['student_ID'] == student_ID:
            print("수강중인 강의코드 입니다.")
            for course in json_big_data[i]['total_course_info']['learning_course_info']:
                print(course['course_code'])

            code = input("수정할 강의 코드를 입력하십시오: ")
            for course in json_big_data[i]['total_course_info']['learning_course_info']:
                if course['course_code'] == code:
                    course[type_name] = change
    save()

while True:
    menu = print_menu()
    if menu == 5:
        save()
        print("학생 정보 관리 프로그램을 종료합니다.")
        break

    while True:
        if menu == 1:
            Input_Student_Info()
        elif menu == 2:
            type = print_menu2()
            if type ==1:
                Total_Search()
            elif type >=2 and type <=9:
                find_key = input("검색어를 입력하세요: ")
                Search(type, find_key)
            elif type == 10:
                break

        elif menu ==3:
            student_id = input("수정할 학생 ID를 입력하세요: ")
            type = print_menu3()
            if type == 0:
                break
            if type >=1 and type <=4:
                alert(type, student_id)
            elif type == 5:
                type2 = print_menu3_5()
                if type2 == 0:
                    break
                alert_course(type2, student_id)

        elif menu == 4:
            type = print_menu4()
            if type == 3:
                break
            student_id = input("삭제할 학생 ID를 입력하세요: ")
            if type == 1:
                delete(student_id)
            elif type == 2:
                delete_course(student_id)




