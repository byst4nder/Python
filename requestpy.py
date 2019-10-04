#! python3
# requests 模块练习  下载网站内容
# 

import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")

# print(type(res))
# print(res.status_code)
# print(len(res.text))
# print(res.text[:300])
# print(res.encoding)

res.raise_for_status()
playfile = open('./file/gutenberg.txt','wb')
for fl in res.iter_content(20000):
    playfile.write(fl)
playfile.close()

