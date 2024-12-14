"""
(编程题)修改百度贴吧的代码，实现任意明星的页面爬取
"""
# import requests

# search = input('请输入你想要搜索的明星名字: ')

# for i in range(0,10):
#     # 获取URL
#     url = f'https://tieba.baidu.com/f?kw={search}&ie=utf-8&pn={i*50}'

#     #发出请求，获取响应
#     res = requests.get(url=url)

#     # 存储数据
#     with open(f'百度贴吧/{search}_{i+1}.html', 'w') as f:
#         f.write(res.text)
#         print(f'{search}第{i+1}页保存成功!')

"""
(编程题)自选一个网站，使用通用爬虫获取五个页面
"""
import requests

for i in range(0, 5):
    url = f'https://www.indeed.com/jobs?q=&l=new+york%2C+ny&sc=0kf%3Aattr%28DSQF7%29%3B&radius=5&start={i*10}'

    res = requests.get(url=url)

    with open(f'自选网站/indeed_{i+1}.html', 'w') as f:
        f.write(res.text)
        print(f'page {i+1} has been saved!')