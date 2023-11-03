import json
import time
from operator import itemgetter
import openpyxl
import requests
import re
json_str = []  # 储存所有json数据
data1 = []
for i in range(1,6):
    time.sleep(1)
    response = requests.get(url='https://oj.qd.sdu.edu.cn/api/problem/list?pageNow='+str(i)+'&pageSize=20')
    page = response.content.decode()
    rs = json.loads(page)
    json_str.append(rs)
#    print(rs)
    temp = rs['data']['rows']
    print(temp)
    for items in temp:
        keys = ['problemId', 'features', 'problemTitle', 'problemCode', 'source', 'remoteOj', 'remoteUrl', 'submitNum', 'acceptNum']
        out = itemgetter(*keys)(items)
        data1.append(out)
print(data1)
wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = 'sheet'
ws1.append(('problemId', 'features', 'problemTitle', 'problemCode', 'source', 'remoteOj', 'remoteUrl', 'submitNum', 'acceptNum'))
for row in data1:
    ws1.append(row)
wb.save('C:\\Users\Lenovo\Desktop\\3.1.1.xls')
