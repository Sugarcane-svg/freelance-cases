import json
import time
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions


chrome_path = r'/Users/phoebezou/Library/Application Support/Google/Chrome/Default'
options = ChromiumOptions()
options.set_browser_path(chrome_path)

page = ChromiumPage(options)
page.get('https://dianqi.suning.com/')

page.ele('#searchKeywords').input('书籍')
page.ele('#searchSubmit').click()

data_list = []
while True:
    time.sleep(2)
    for i in range(4):
        
        page.run_js('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)

    all_div = page.eles('x://div[@class="product-box "]/div[@class="res-info"]')

    for i in all_div:
        data_dict = {}
        data_dict['price'] = i.ele('.price-box').text
        data_dict['selling_point'] = i.ele('.title-selling-point').text
        data_dict['store'] = i.ele('.store-stock').text

        data_list.append(data_dict)

    try:
        page.ele('#nextPage').click()
    except:
        break

page.close()

with open('苏宁易购书籍.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=4)



    