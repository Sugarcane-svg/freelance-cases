"""
(编程题)给定url="https://www.xs8.cn/book/20664751308717404#Catalog"
请你获取小说章节名及小说文本，存储为txt文件
"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.xs8.cn/book/20664751308717404'
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

res = requests.get(url, headers = headers)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

all_li = soup.select('div.volume>ul.cf>li')

for i in all_li:
    chapter_name = i.text
    chapter_url = 'https://www.xs8.cn' + i.select('a')[0]['href']
    content_res = requests.get(chapter_url, headers=headers)
    content_res.encoding = 'utf-8'
    content_soup = BeautifulSoup(content_res.text, 'html.parser')
    content = content_soup.select('div.ywskythunderfont>p')[0].text

    # break
    with open(f'女配画风不对/{chapter_name}.txt', 'w', encoding='utf-8') as f:
        f.write(content)
