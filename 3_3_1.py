import json
from operator import itemgetter
import openpyxl
import requests
from bs4 import BeautifulSoup
import re
import time
json_str = []  # 储存所有json数据
data1 = []
list1 = []
list2 = []
list_title = []
list_href = []
list_date = []
list_time =[]
for i in range(1, 20):
    time.sleep(1)
    response = requests.get(url='https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=168&PAGENUM=' + str(i) + '&urltype=tree.TreeTempUrl&wbtreeid=1010')
    time.time()
    for j in range(1, 16):
        list_time.append(time.asctime())
    page = response.content.decode()
    soup = BeautifulSoup(page, 'html.parser')
    script1 = soup.find_all('a', attrs={"target": "_blank", "style": ""})
    list1.append(script1)
    script2 = soup.find_all('div', attrs={"style": "float:right;"})
    list2.append(script2)
#   print(list2)
str1 = ""
for items in list1:
    str1 = str1 + str(items) + ""
list_title = re.findall(r'<a.*?>(.*?)</a>', str1)
#   print(list_title)

str2 = ""
for items in list1:
    str2 = str2 + str(items) + ""
list_href1 = re.findall('<a[^>]+href=["\']c(.*?)["\']', str2)
list_href = ["c"+str(items) for items in list_href1]
#   print(list_href)

str3 = ""
for items in list2:
    str3 = str3 + str(items) + ""
list_date = re.findall('<div style="float:right;">(.*?)</div>', str3)
#   print(list_date)


print(list_time)
li = list(zip(list_title, list_href, list_date, list_time))
print(li)
wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = 'sheet'
ws1.append(('list_title', 'list_href', 'list_date', 'list_time'))
for row in li:
    ws1.append(row)
wb.save('C:\\Users\Lenovo\Desktop\\3.3.1.xls')


