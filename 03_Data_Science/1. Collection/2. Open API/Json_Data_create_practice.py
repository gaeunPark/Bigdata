import json
with open('ITT_Student.json', encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)

find_key = '김기'
count = 0
student_ID = []

for Student in json_big_data:
    if Student['student_ID'].find(find_key) != 0:
        count += 1
        student_ID.append(Student['student_ID'])
    else:
        print("찾는값이 없습니다.")
print(count)

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



a = {'a':1, 'b':2, 'c':3}
print(a.keys())

for i in a.keys():
    print(i)



# print(json_big_data[0]['total_course_info']['learning_course_info'][0]['course_name'])
# print("1" + '1')



