import csv
import json

with open("이명박_naver_news.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)

print("데이터 분석을 시작합니다.")
data = []
# org_link 분리
for org_link in jsonResult:
   data.append(org_link['org_link'])

link = []
blank_count = 0

for i in data:
    try:
        link.append((i.split('/'))[2])
    except:
        blank_count += 1
        print('org_link가 없는 기사를 발견했습니다.')
print()

distint_link = set(link)

print('<네이버 검색 빅데이터 분석>')
print('검색어: 이명박')
print('전체 도메인 수: %d' %len(distint_link) )
print('전체 건수: %d' %len(link))
print('부정확한 데이터수: %d' %blank_count)
print()

list = []
for distint in distint_link:
    count = 0
    domain= []
    for i in link:
        if distint == i:
            count += 1
    domain.append(distint)
    domain.append(count)
    list.append(domain)

list = sorted(list, key = lambda aa: aa[1], reverse=True)

print('-도메인 별 뉴스 기사 분석')
for i in list:
    print('>> %s: %d건' %(i[0], i[1]))