#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 14:44
# @Author  : Xuegod Teacher For
# @File    : 01_linajia_test.py
# @Software: PyCharm
import requests  # pip install requests
from fake_useragent import UserAgent
from lxml import etree

headers = {
    'User-Agent':UserAgent().random
}
urlzf =r'https://cq.lianjia.com'

for x in range(1,3):
    url = r'https://cq.lianjia.com/zufang/pag{}'.format(x)


    response = requests.get(url=url,headers=headers)
    #这是吧文本转换为xpath课匹配的文本
    xpath_content = etree.HTML(response.text)
    # print(response.text)
    #利用xpath匹配
    data = xpath_content.xpath('//*[@id="content"]/div/div/div/div/p[1]/a/text()')
    data11 = xpath_content.xpath('//*[@id="content"]/div/div/div/div/p[1]/a/@href')
    data2 = xpath_content.xpath('//*[@id="content"]/div/div/div/div/span/em/text()')
    data21 = xpath_content.xpath('//*[@id="content"]/div/div/div/div/span/text()')
    data3=xpath_content.xpath('//*[@id="content"]/div/ul/li/a/@href')

# //div/div[2]/a/@href
# //*[@id="content"]/div[1]/div[2]/a[2]

    #返回列表数据
    for i in range(0,len(data2)):
        # pass
        print(x,i,data[i],data2[i],data21[i],urlzf+data11[i])
    #输出每一页中页码链接
    for i in range(0,len(data3)):
        print(x,i,urlzf+data3[i])
    # print(data3)
# print(xpath_content)
# print(type(xpath_content))
#响应状态码
# print(response.status_code)
#响应体，字符窜
# print(response.text)
#二进制表达
# print(response.content)
