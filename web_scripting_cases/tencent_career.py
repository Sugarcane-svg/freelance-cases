"""
(编程题)给定url='https://careers.tencent.com/search.html?keyword=Python'
请你获取当前url中关于：岗位的名称、所在地、更新日期
"""



import requests

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

with open('tencent_career.csv','w') as f:
    f.write('position_name|location_name|last_updated_time\n')


for i in range(3):

    url = f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1732332586930&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=Python&pageIndex={i+1}&pageSize=10&language=zh-cn&area=us'


    res = requests.get(url, headers=headers)

    
    for j in res.json()['Data']['Posts']:
        recruitPostName = j['RecruitPostName']
        locationName = j['LocationName']
        lastUpdateTime = j['LastUpdateTime']

        with open('tencent_career.csv', 'a') as f:
            f.write('|'.join([recruitPostName, locationName, lastUpdateTime]) + '\n')
        
        



