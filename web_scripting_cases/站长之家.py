"""
(编程题)将上课的站长之家完善, url = https://top.chinaz.com/hangye/
获取排行页以及详情页信息：
    排行页：网页名称，详情页url
    详情页：排名， 地区， 网站类型
"""
import requests
from bs4 import BeautifulSoup
import json

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

data_list = []
for i in range(1, 4):

    if i == 1:

        url = 'https://top.chinaz.com/hangye/'

    else:

        url = f'https://top.chinaz.com/hangye/index_{i}.html'

    
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'

    soup = BeautifulSoup(res.text, 'html.parser')

    all_li = soup.select('ul.listCentent>li')
    
    for j in all_li:

        data_dict = {}

        data_dict['site_name'] = j.select('h3.rightTxtHead>a')[0].text
        data_dict['site_url'] = 'https://top.chinaz.com' + j.select('h3.rightTxtHead>a')[0]['href']


        # 提取详情页信息
        detail_res = requests.get(url = data_dict['site_url'], headers = headers)
        detail_res.encoding = 'utf-8'

        detail_soup = BeautifulSoup(detail_res.text, 'html.parser')
        detail_all_li = detail_soup.select('ul.TopMain-left>li')

        data_dict['overall_rank'] = detail_all_li[0].select('p.headpoint>a')[0].text.strip()
        data_dict['area'] = detail_all_li[1].findAll('p')[1].text
        data_dict['website_type'] = detail_all_li[2].findAll('p')[1].text

        data_list.append(data_dict)

    
with open('站长之家.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=4)


        

