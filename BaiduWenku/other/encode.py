import requests
import re
import json
import time



# url = r'https://wenku.baidu.com/view/395f45b35122aaea998fcc22bcd126fff6055d0f.html'
url = r'https://wenku.baidu.com/view/25cce92554270722192e453610661ed9ad5155aa.html'

url = r'https://wenku.baidu.com/view/8c3acd03ff4733687e21af45b307e87101f6f820.html'

header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "wenku.baidu.com",
    "Origin": "https://wenku.baidu.com",
    # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }


head = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "wkbjcloudbos.bdimg.com",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}


r = requests.get(url= url,headers = header)
rco = r.content.decode('gbk')
print(rco)
with open('wk2.txt','w',encoding='utf-8') as f:
    f.write(rco)


ll = re.findall('[,\[]{.{10,30}:(\d{1,3}).{10,30}(https:.*?\.json\?.*?token.*?)\\\\x22}',rco)
dic = {}
for i in ll:
    # dic[i[0]] = i[1].replace('\\\\\\/','/').encode('utf-8').decode('unicode_escape', 'ignore')
    print(i[1])
    dic[i[0]] = i[1].replace('\\','').encode('utf-8').decode('unicode_escape', 'ignore')


for x,y in dic.items():
    print(x,':',y)
    r2 = requests.get(url = y, headers = head)
    # json_data = re.search('{.*}',r2.content.decode('unicode_escape', 'ignore')).group(0)
    json_data = re.search('{.*}',r2.content.decode('unicode_escape', 'ignore')).group(0)


    da = json.loads(json_data)['body']
    # print('da',da)
    da_j = ''
    for i in da:
        # print('1',type(i),type(i['c']),i['c'])
        if type(i['c']) == str:
           da_j += i['c'].strip()

    # rdata = r2.text.encode('utf-8').decode('unicode_escape', 'ignore')
    # print(type(rdata),rdata)
    # print(json_data)
    print(da_j)
    time.sleep(3)

