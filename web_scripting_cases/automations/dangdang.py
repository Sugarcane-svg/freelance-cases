"""
获取当当网任意内容
"""
import json
import time
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.dangdang.com')
time.sleep(2)
page.ele('#key_S').input('连衣裙')
time.sleep(3)
page.ele('x://input[@class = "button"]').click()
time.sleep(2)
data_list = []

while page.ele('x://div[@class="paging"]/ul/li[4]/a').text == "3":
    all_li = page.eles("x: //ul[@id = 'component_59']/li")

    for i in all_li:
        data_dict = {}
        try:
            data_dict['price'] = i.ele('x:/p[@class = "price"]/span', timeout = 0.1).text
        except:
            data_dict['price'] = "NA"
        try:
            data_dict['title'] = i.ele('x:/p[@class = "name"]/a[@dd_name = "单品标题"]', timeout = 0.1).text
        except:
            data_dict['title'] = "NA"
        try:
            data_dict['store'] = i.ele('x:/p[@class = "link"]/a', timeout = 0.1).text
        except:
            data_dict['store'] = "NA"

        data_list.append(data_dict)
        # print(data_dict)
    
    

    try:
        page.ele('x://li[@class="next"]').click()
        time.sleep(2)
    except:
        break

with open("当当网连衣裙.json", "w", encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=4)
