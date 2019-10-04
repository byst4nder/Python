import requests
import bs4
# res = requests.get(r'http://www.gutenberg.org/cache/epub/1112/pg1112.txt')


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
} 

res = requests.get(url=r'http://www.baidu.com/s?wd=github&pn=0',headers=headers,allow_redirects=False)
res.raise_for_status()
# print(res.text[0:1000])
noStarchSoup = bs4.BeautifulSoup(res.text,features="html.parser")
# print(type(noStarchSoup))  #<class 'bs4.BeautifulSoup'>
# elems = noStarchSoup.select('div h3 a[href]') 
# for i in range(0,len(elems)):
#     print(i,elems[i].get('href')) 


elems = noStarchSoup.select('.t a[href]') 
for i in range(0,len(elems)):
    href=elems[i].get('href')
    baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
    real_url = baidu_url.headers['Location']
    print(type(href),type(baidu_url),type(real_url))
    print(i,href) 
    print(i,real_url) 
# print('1',type(elems))  #<class 'list'>
# print('2',len(elems))  # 9
# print('3',type(elems[0]))  #<class 'bs4.element.Tag'>
# print('4',elems[0].getText()) #
# print('5',str(elems[0]))
# print('6',elems[0].attrs)  #{'id': 'wrapper'}
 