"""
给定网站：https://500px.com.cn/community/search/user  获取摄影师名称，图片数量，粉丝数；进入详情页获取用户ID属地
"""

import requests
import openpyxl

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

data_list = []
for i in range(1, 4):
    url = f'https://500px.com.cn/community/user-details/userInfos?page={i}&size=20&type=json'

    res = requests.get(url, headers=headers)

    for i in res.json():
        data_dict = {}
        data_dict['nickName'] = i['nickName']
        data_dict['userUploaderCount'] = i['userUploaderCount']
        data_dict['userFollowedCount'] = i['userFollowedCount']
        profile_target = 'https://500px.com.cn/community/v2/user/indexInfo?queriedUserId=' + i['id']

        profile_res = requests.get(url= profile_target, headers=headers)

        data_dict['IP'] = profile_res.json()['data']['userAdress']

        data_list.append(data_dict)
        # print(data_dict)

    
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["昵称",'上传数量', '粉丝数', "IP"])
for v in data_list:
    row = [i for i in v.values()]
    ws.append(row)

wb.save("摄影数据.xlsx")





