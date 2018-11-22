import urllib.request
import datetime
import json

access_key="yZZgPPuDihT%2F%2BxPnqlmB43yjAdza8%2F23DVjtbXpxc5peeqF9Mu%2FADaBFPgXYSxzXG6pXJtdQJzUdiFIVQMsg4Q%3D%3D"

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

def get_Weather_info(yyyymmdd, time, nx, ny, nItems):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + time
    parameters += "&nx=" + str(nx)
    parameters += "&ny=" + str(ny)
    parameters += "&numOfRows=" + str(nItems)

    url = end_point + parameters
    retData = get_request_url(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

def append_Weather_Data(item, jsonResult):
    baseDate = '' if 'baseDate' not in item.keys() else item['baseDate']
    baseTime = '' if 'baseTime' not in item.keys() else item['baseTime']
    category = '' if 'category' not in item.keys() else item['category']
    fcstDate = '' if 'fcstDate' not in item.keys() else item['fcstDate']
    fcstTime = '' if 'fcstTime' not in item.keys() else item['fcstTime']
    fcstValue = '' if 'fcstValue' not in item.keys() else item['fcstValue']
    nx = 0 if 'nx' not in item.keys() else item['nx']
    ny = 0 if 'ny' not in item.keys() else item['ny']

    jsonResult.append({'baseDate': baseDate,
                       'baseTime': baseTime,
                       'category': category,
                       'fcstDate': fcstDate,
                       'fcstTime': fcstTime,
                       'fcstValue': fcstValue,
                       'nx': nx,
                       'ny': ny})
    return

def get_Realtime_Weather():
    # 00~29: 정확히 30분 뺄 것
    # 30~59: 실시간 update
    hour = datetime.datetime.now().strftime('%H')
    minute = datetime.datetime.now().strftime('%M')
    time = datetime.datetime.now().strftime('%H%M')

    print('<기상정보 업데이트>')
    hour = int(hour); minute = int(minute)

    if 0< minute < 29:
        hour -= 1
        minute = 60 + (minute-30)
        time = str(hour) + str(minute)
    return time

def main():
    jsonResult = []
    yyyymmdd = datetime.datetime.now().strftime('%Y%m%d')
    time = get_Realtime_Weather()
    nx = 89
    ny = 91
    nItems = 100

    while True:
        jsonData = get_Weather_info(yyyymmdd, time, nx, ny, nItems)

        if(jsonData['response']['header']['resultMsg'] == 'OK'):
            nTotal = jsonData['response']['body']['totalCount']
            if nTotal == 0:
                break
            for item in jsonData['response']['body']['items']['item']:
                append_Weather_Data(item, jsonResult)
                nTotal -= 1
            if nTotal == 0:
                break
        else:
            break

    with open('신암동_초단기예보조회.json', 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()