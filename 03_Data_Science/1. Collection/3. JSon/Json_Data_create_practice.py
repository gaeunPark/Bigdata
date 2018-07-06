import json
with open('ITT_Student.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)

def Search_ID(student_ID):
    for Student in json_big_data:
        if Student['student_ID'] == student_ID:
            print("""* 학생 ID: %s 
* 학생 이름: %s
""" % (Student['student_ID'], Student['student_name']))





# find_key = '현구'
# count = 0
# student_ID = []
#
# for Student in json_big_data:
#     if Student['total_course_info']['learning_course_info'][0]['teacher'].find(find_key) != -1:
#         count += 1
#         student_ID.append(Student['student_ID'])
#
# for ID in student_ID:
#     if count == 1:
#         Search_ID(ID)
#     elif count >=2:
#         Search_ID(ID)
#     elif count == 0:
#         print("찾는값이 없습니다.")

a = [{1:1, 2:2}, {1:1, 2:2}]
print(a)
del a[0]
print(a)


# with open('ITT_Student.json', encoding='UTF8') as json_file:
#     json_object = json.load(json_file)
#     json_string = json.dumps(json_object)
#     json_big_data = json.loads(json_string)
#
#     for Student in json_big_data:
#         print("""* 학생 ID: %s
# * 이름: %s
# * 나이: %s
# * 주소: %s
# * 수강 정보
#  + 과거 수강 횟수: %s""" %( Student['student_ID'], Student['student_name'], Student['student_age'], Student['address'], Student['total_course_info']['num_of_course_learned']))



