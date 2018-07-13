# XML_URL: http://nenechicken.com/subpage/where_list.asp
# py -m pip install pandas
import urllib.request
from pandas import DataFrame
print('XML 데이터 수집 연습예제 구동')
result = []

import xml.etree.ElementTree as ET
response = urllib.request.urlopen('')

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)