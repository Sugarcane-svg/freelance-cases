"""
(编程题)给定 url='http://www.360doc.com/content/23/1221/04/70011493_1108271406.shtml'
需求：提取出排名、名字、年龄、财富值、财富来源，并存储为json文件
"""
import requests
from lxml import etree
import json

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

url = 'http://www.360doc.com/content/23/1221/04/70011493_1108271406.shtml'

data_list = []

# get response
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'

# convert text into html
web_page = etree.HTML(res.text)

# get the table -> tbody
all_tr = web_page.xpath('//table[@width="100%"]/tbody/tr')

for i in all_tr[1:]:

    data_dict = {}
    data_dict['排名'] = i.xpath('./td[1]/text()')[0]
    data_dict['姓名'] = i.xpath('./td[2]/p/text() | ./td[2]/br')[0]
    if type(data_dict['姓名']) == etree._Element:
        data_dict['姓名'] = ''
    data_dict['年龄'] = i.xpath('./td[3]/text()')[0]
    data_dict['财富值'] = i.xpath('./td[4]/text()')[0]
    data_dict['财富来源'] = i.xpath('./td[5]/text() | ./td[5]/br')[0]
    if type(data_dict['财富来源']) == etree._Element:
        data_dict['财富来源'] = ''


    data_list.append(data_dict)

    # print(i.xpath('./td[2]/p/text() | ./td[2]/br')[0], type(i.xpath('./td[2]/p/text() | ./td[2]/br')[0]))

with open('json_files/福布斯富豪榜.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent = 4)

# print(data_list)
