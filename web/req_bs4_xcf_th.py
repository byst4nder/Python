#! python
# 下载 下厨房网站首页图片
# 多线程

import os
import time
import struct
import threading
from urllib.parse import urlparse
import bs4
import requests
import lxml



def check_path(filepath):
    if not os.path.isdir(filepath):
        os.mkdir(filepath)
    return filepath

def getname(url):
    return  urlparse(url).path.split('@')[0].split('/')[-1][1:]

def url_check(url):
    o =urlparse(url)
    return '%s://%s%s' % (o.scheme,o.netloc,o.path.split('@')[0])

def down_img(img_all:dict):
    global look_dir
    print('thread %s is running...' % threading.current_thread().name)
    i = 0
    for img in img_all.keys():

        if  img_all[img] :
            continue
        else:
            img_all[img] = 1
        o = urlparse(img)
        filename = o.path[1:].split('@')[0]
        filepath = os.path.join(bspath, filename).replace('/', '\\')
        if not os.path.isdir(os.path.dirname(filepath)):
            while True:
                if look_dir == 1:
                    continue
                else:
                    look_dir = 1
                    os.mkdir(os.path.dirname(filepath))
                    look_dir = 0
                    break
        imgurl = url_check(img)
        i += 1
        print('{}-{}\t{}\n'.format('%s正在下载%s:'% (threading.current_thread().name,i), imgurl, filepath),end='')
        resp = requests.get(imgurl)
        with open(filepath, 'wb') as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)





if __name__ == '__main__':
    global look_dir
    look_dir = 0
    url = 'http://www.xiachufang.com/'
    # TODO 打开网页，获取网页
    chuf = requests.get(url)
    bspath=check_path(os.path.join(os.curdir,'img'))
    #  解析图片网址,并保存到img_list列表
    bs = bs4.BeautifulSoup(chuf.text,'lxml')
    open(os.path.join(bspath,'xcf.html'),'w',encoding='utf-8').write(bs.prettify())

    img_all = { }
    for img in bs.find_all('img'):
        if img.has_attr('data-src'):
            img_all[img.attrs['data-src']] = 0
        else:
            img_all[img.attrs['src']] = 0

    # 下载并保存网页
    for i in range(10):
        threadName = 't{}'.format(i)
        threadName = threading.Thread(target=down_img,args=(img_all,))
        threadName.start()



