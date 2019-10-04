#! python3
# 搜索关键词 并获取搜索结果，并解析网址

import bs4
import urllib
import bs4
import requests

word = 'github'
url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn=0' # word为关键词，pn是百度分页
response = urllib.request.urlopen(url)
page = response.read()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    } #定义头文件，伪装成浏览器

all = open(r'.\file\test.txt', 'a')

soup = bs4.BeautifulSoup(page, 'lxml')
tagh3 = soup.find_all('h3')
for h3 in tagh3:
    href = h3.find('a').get('href')
    baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
    real_url = baidu_url.headers['Location']  #得到网页原始地址
    if real_url.startswith('http'):
        all.write(real_url + '\n')
        print(href)
        print(real_url)
 


