import json
# bigdata = []
# student_ID = 'ITT001'
# student_age = '24'
# student_name ='박가은'
# address = '대구광역시 동구 아양로 135): '
# course_code = 'IB171106'
# course_name = 'IOT빅데이터 실무반'
# teacher = '이현구'
# open_date = '2017-11-06'
# close_date = '2018-09-05'
# num_of_course_learned = '1'
#
# bigdata.append(
# {
#         "address": address,
#         "student_ID": student_ID,
#         "student_age": student_age,
#         "student_name": student_name,
#         "total_course_info": {
#             "learning_course_info": [
#                 {
#                     "close_date": close_date,
#                     "course_code": course_code,
#                     "course_name": course_name,
#                     "open_date": open_date,
#                     "teacher": teacher
#                 }
#             ],
#             "num_of_course_learned": num_of_course_learned
#         }
# }
# )
# print('프로그램 종료')



# Student_info_list['address'] = address
# Student_info_list['student_ID'] = student_ID
# Student_info_list['student_age'] = student_age
# Student_info_list['student_name'] = student_name
# Student_info_list['total_course_info'] = total_course_info

# course_info['close_date'] = close_date
# course_info['course_code'] = course_code
# course_info['course_name'] = course_name
# course_info['open_date'] = open_date
# course_info['teacher'] = teacher



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



