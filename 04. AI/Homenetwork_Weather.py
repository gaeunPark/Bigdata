import urllib.request
import datetime
import json
import os

access_key="yZZgPPuDihT%2F%2BxPnqlmB43yjAdza8%2F23DVjtbXpxc5peeqF9Mu%2FADaBFPgXYSxzXG6pXJtdQJzUdiFIVQMsg4Q%3D%3D"
base_dir_name = 'V3_BigData'
dir_delimeter = '\\'
level2_dir = 'weather_info'
file_limit = 3

def make_base_dir():
    os.makedirs('.' + dir_delimeter + base_dir_name)

def make_d2_dir(dir_num):
    os.makedirs('.' + dir_delimeter + base_dir_name + dir_delimeter + level2_dir + dir_num)

def directory_num():
    dir_num = len(os.listdir('.' + dir_delimeter + base_dir_name))
    if len(os.listdir('.' + dir_delimeter + base_dir_name + dir_delimeter + level2_dir + str(dir_num))) == file_limit:
        dir_num += 1
        make_d2_dir(str(dir_num))
    return str(dir_num)

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" %(datetime.datetime.now(), url))
        return None

def get_Weather_URL():
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + time
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += "&numOfRows=100"

    url = end_point + parameters
    retData = get_request_url(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

def Make_weather_Json():
    jsonData = get_Weather_URL()

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for item in jsonData['response']['body']['items']['item']:
            jsonResult.append({'baseDate': item['baseDate'],
                               'baseTime': item['baseTime'],
                               'category': item['category'],
                               'fcstDate': item['fcstDate'],
                               'fcstTime': item['fcstTime'],
                               'fcstValue': item['fcstValue'],
                               'nx': item['nx'],
                               'ny': item['ny']})

    with open('.%s%s%s%s%s%s신암동_초단기예보조회_%s%s%s.json' \
              %(dir_delimeter, base_dir_name, dir_delimeter, level2_dir, directory_num(), dir_delimeter, yyyymmdd, time, sec),\
              'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def get_Realtime_Weather():
    hour = datetime.datetime.now().strftime('%H')
    minute = datetime.datetime.now().strftime('%M')
    time = datetime.datetime.now().strftime('%H%M')
    print('<기상정보 업데이트>')
    hour = int(hour)
    minute = int(minute)

    if 0< minute < 29:  # 00~29: 정확히 30분 뺄 것
        hour -= 1       # 30~59: 실시간 update
        minute = 60 + (minute-30)
        time = "{0:0>2}".format(hour)  + str(minute)
    return time


jsonResult = []
yyyymmdd = datetime.datetime.now().strftime('%Y%m%d')
time = get_Realtime_Weather()
sec = datetime.datetime.now().strftime('%S')
nx = '89'
ny = '91'

if not os.path.exists('.' + dir_delimeter + base_dir_name):
    make_base_dir()
if not os.path.exists('.' + dir_delimeter + base_dir_name + dir_delimeter + level2_dir + '1'):
    make_d2_dir('1')

Make_weather_Json()
