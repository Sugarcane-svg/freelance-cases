"""
(编程题)给定目标:http://www.ccgp-hunan.gov.cn/page/notice/more.jsp
获取公告数据，存储为json文件
"""
import requests
import json


url = 'http://www.ccgp-hunan.gov.cn/mvc/getNoticeList4Web.do'

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

data = {
    'pType': '',
    'prcmPrjName': '',
    'prcmItemCode': '',
    'prcmOrgName': '',
    'startDate': '2024-01-01',
    'endDate': '2024-11-24',
    'prcmPlanNo': '',
    'page': 1,
    'pageSize': 18
}

res = requests.post(url, headers=headers, data = data)

d_list = []
for i in res.json()['rows']:
    d_dict = {}
    
    d_dict['AREA_NAME'] = i['AREA_NAME']
    d_dict['NOTICE_NAME'] = i['NOTICE_NAME']
    d_dict['PRCM_MODE_NAME'] = i['PRCM_MODE_NAME']
    d_dict['ORG_CODE'] = i['ORG_CODE']
    d_dict['NOTICE_TITLE'] = i['NOTICE_TITLE']
    d_dict['NEWWORK_DATE'] = i['NEWWORK_DATE']

    d_list.append(d_dict)

with open('湖南政府采购.json', 'w', encoding='utf-8') as f:
    json.dump(d_list, f, ensure_ascii=False, indent=4)



