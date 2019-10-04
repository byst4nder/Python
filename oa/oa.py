
import requests
import os
import re
import json

from lxml import etree
from bs4 import  BeautifulSoup


if __name__ == '__main__':

    url = 'http://oa.cqszfy.com:10000'

    filepath = os.path.join(os.curdir,'file')
    if not os.path.isdir(filepath):
        os.mkdir(filepath)
    # TODO 打开oa登录页，并登录

    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    header = {
        "Referer": "http://oa.cqszfy.com:10000/",
        'User-Agent': userAgent,
    }


    prm = {
               "loginfile" : "/wui/theme/ecology8/page/login.jsp?templateId=21&logintype=1&gopage=",
                "logintype" : "1",
                "fontName" : "微软雅黑",
                "message" : "",
                "gopage" : "",
                "formmethod" : "post",
                "rnd" : "",
                "serial" : "",
                "username" : "",
                "isie" : "false",
                "weaverssoservice" : "",
                "appid" : "",
                "islanguid" : "7",
                "loginid" : "61309011",
                "userpassword" : "wl123456",
                "tokenAuthKey" : ""
    }
    # data = 'loginfile=%2Fwui%2Ftheme%2Fecology8%2Fpage%2Flogin.jsp%3FtemplateId%3D21%26logintype%3D1%26gopage%3D&logintype=1&fontName=%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91&message=&gopage=&formmethod=post&rnd=&serial=&username=&isie=false&weaverssoservice=&appid=&islanguid=7&loginid=61309011&userpassword=wl123456&tokenAuthKey='
    posturl = 'http://oa.cqszfy.com:10000/login/VerifyLogin.jsp'
    # posturl = 'http://httpbin.org/post'
    req_session = requests.session()
    resp = req_session.post(posturl,headers=header,data=prm)
    cookie_dict = requests.utils.dict_from_cookiejar(resp.cookies)
    print(cookie_dict)
    with open('cookies.json','w',encoding='utf-8') as f:
        json.dump(cookie_dict,f)
    # print(cookie)

    with open('cookies.json','r',encoding='utf-8') as f:
        cook = requests.utils.cookiejar_from_dict(json.load(f))

    # print(cook)
    # req_main_session = requests.session(cook)
    resp_main = requests.get('http://oa.cqszfy.com:10000/wui/main.jsp',headers=header,cookies = cook)
    print(resp_main.text)

    # resp_main_hs = req_session.get('http://oa.cqszfy.com:10000/homepage/Homepage.jsp?hpid=2&subCompanyId=1&isfromportal=1&isfromhp=0',headers=header)
    # resp_file = req_session.get('http://oa.cqszfy.com:10000/page/element/7/News.jsp?ebaseid=7&eid=101&styleid=1390381555293&hpid=2&subCompanyId=1&e71566564304285=&pagetype=&fieldids=&fieldvalues=',headers=header)
    #
    # resp_file_search = req_session.get('http://oa.cqszfy.com:10000/docs/search/DocSearchTab.jsp?urlType=16&eid=101&tabid=3&date2during=0',headers=header)
    # resp_file_open = req_session.get(
    #     'http://oa.cqszfy.com:10000/docs/docs/DocDsp.jsp?id=65346',
    #     headers=header)
    # resp_file_open = req_session.get(
    #     'http://oa.cqszfy.com:10000/docs/docs/DocDsp.jsp?id=65346',
    #     headers=header)
    #
    #
    # print(resp_file_open.status_code)
    # print(resp.headers['Location'])
    # print(resp_file_open.text)
    # TODO 进入医院门户，获取医院门户信息
    # TODO 进入个人门户，获取个人门户信息
    # TODO 下载文件
    # TODO
    # TODO
