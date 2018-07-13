import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import os

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# print(soup.prettify())

result =[]
name_list = []
range_list = []
up_down_list = []

tags =  soup.findAll('div', attrs={'class':'tit3'})
for tag in tags:
    name_list.append(tag.a.string)

up_down_info = soup.findAll('img', attrs={'class':'arrow'})
for up_down in up_down_info:
    up_down_list.append(up_down.attrs['alt'])

range_info = soup.findAll('td', attrs={'class':'range ac'})
for ranges in range_info:
    range_list.append(ranges.string)

for i in range(0,50):
    result.append({
        'rank': str(i+1),
        'name': name_list[i],
        'range': range_list[i],
        'up_down': up_down_list[i]
    }
    )

rank_table = DataFrame(result, columns=('rank','name','range', 'up_down'))




f = open('file_idx.txt', 'r', encoding='utf-8')
lines = f.readline()
if lines == "":
    file_num = 0
else:
    file_num = lines[-1]
f.close()

dir_name = 'naver_ranking'
csv = '.csv'
dem = '\\'
upper_dir = 'V2_BIGDATA\\'
file_num= int(file_num)
if file_num == 0:
    dir_num = 1
    os.makedirs(upper_dir + dir_name + str(dir_num))
elif file_num % 3 == 0:
    dir_num = int(file_num/3) + 1
    os.makedirs(upper_dir + dir_name + str(dir_num))
elif file_num % 3 != 0:
    dir_num = int(file_num/3) + 1


file_num = str(int(file_num) + 1)

dir_name = dir_name + str(dir_num)

file_name = 'movie' + file_num + csv
file_path = upper_dir + dir_name + dem

rank_table.to_csv(file_path + file_name, encoding="utf-8", mode='w', index=False)


f = open('file_idx.txt', 'a', encoding='utf-8')
f.write(file_num)
f.close()