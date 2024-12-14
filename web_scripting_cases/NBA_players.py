"""
(自己尝试)给定 url='https://china.nba.cn/playerindex' or url = 'https://www.nba.com'
点击球员->现役球员
需求：获取球员中文名称、英文名称、所属球队、球衣号码、位置等信息
"""
import requests
from lxml import etree
import json

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
url = 'https://www.nba.com/players'


res = requests.get(url, headers = headers)

res_html = etree.HTML(res.text)

all_tr = res_html.xpath('//tbody/tr')

data_list = []
for i in all_tr:
    data_dict = {}
    data_dict['name'] = ' '.join(i.xpath('./td[1]/a/div[2]/p/text()'))
    data_dict['team'] = i.xpath('./td[2]/a/text()')[0]
    data_dict['number'] = i.xpath('./td[3]/text()')[0]
    data_dict['position'] = i.xpath('./td[4]/text()')[0]
    data_dict['height'] = i.xpath('./td[5]/text()')[0]
    data_dict['weight'] = i.xpath('./td[6]/text()')[0] + ' lbs'
    data_dict['last attended'] = i.xpath('./td[7]/text()')[0]
    data_dict['country'] = i.xpath('./td[8]/text()')[0]

    data_list.append(data_dict)
    
# with open('json_files/NBA_players.json', 'w') as f:
#     json.dump(data_list, f, indent=4)

print(len(data_list))
    
