import json

with open('ITT_Student.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)

f = open('D:/Python_Workspace/03_Data_Science/1. Collection/2. Open API/ITT_student_ID.txt', 'r', encoding='utf-8')
idxes = f.readlines()
idx = idxes[-1]
f.close()
# print(idx[:3] + str(int(idx[3:])+1))

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

def Search(type, find_key):
    if type == 2: type = 'student_ID'
    elif type == 3: type = 'student_name'
    elif type == 4: type = 'student_age'
    elif type == 5: type = 'address'
    elif type == 6: type = 'num_of_course_learned'
    elif type == 7: type = 'learning_course_info'
    elif type == 8: type = 'course_name'
    elif type == 9: type = 'teacher'

    count = 0
    student_ID = []


    for Student in json_big_data:
        if type>=2 and type<=5:
            if find_key == Student[type]:
                count += 1
                student_ID.append(Student['student_ID'])
        elif type == 6:
            if find_key == Student['total_course_info'][type]:
                count += 1
                student_ID.append(Student['student_ID'])
        elif type ==7:
            if find_key == Student['total_course_info']['learning_course_info']:
                count += 1
                student_ID.append(Student['student_ID'])
        elif type>=8:
            if find_key == Student['total_course_info']['learning_course_info'][type]:
                count += 1
                student_ID.append(Student['student_ID'])

    if count == 1:
        Search_ID(student_ID[0])
    elif count >=2:
        print(student_ID)
    elif count == 0:
        print("찾는 값이 없습니다.")

while True:
    menu = print_menu()

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
            print("")






    if menu == 5:
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('ITT_Student.json SAVED')
        print("학생 정보 관리 프로그램을 종료합니다.")
        break

    # elif menu == 4:
    #     ID = input('삭제할 학생 ID를 입력하세요: ')
    #     type = input("""삭제 유형을 선택하세요.
    #     1. 전체 삭제
    #     2. 현재 수강 중인 특정 과목 정보 삭제
    #     3. 이전 메뉴
    #     메뉴 번호를 선택하세요: """)

