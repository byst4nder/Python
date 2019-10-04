import os
import struct
# from threading import Thread  # 多线程模块
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

def down_img(img_list):
    print('thread %s is running...' % threading.current_thread().name)
    for img in img_list:
        o = urlparse(img)
        filename = o.path[1:].split('@')[0]
        filepath = os.path.join(bspath, filename).replace('/', '\\')
        if not os.path.isdir(os.path.dirname(filepath)):
            os.mkdir(os.path.dirname(filepath))
        imgurl = url_check(img)
        print('{}-{}\t{}\n'.format('%s正在下载:'% threading.current_thread().name, imgurl, filepath),end='')
        resp = requests.get(imgurl)
        with open(filepath, 'wb') as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)

if __name__ == '__main__':

    url = 'http://www.xiachufang.com/'
    # TODO 打开网页，获取网页
    chuf = requests.get(url)
    bspath=check_path(os.path.join(os.curdir,'img'))

    #  解析图片网址,并保存到img_list列表
    bs = bs4.BeautifulSoup(chuf.text,'lxml')
    open(os.path.join(bspath,'xcf.html'),'w',encoding='utf-8').write(bs.prettify())

    img_list = []
    for img in bs.find_all('img'):
        if img.has_attr('data-src'):
            img_list.append(img.attrs['data-src'])
        else:
            img_list.append(img.attrs['src'])

    # 下载并保存网页
    thread_con=len(img_list)//4
    t1 = threading.Thread(target=down_img,args=(img_list[:thread_con],))
    t1.start()
    t2 = threading.Thread(target=down_img,args=(img_list[thread_con+1:thread_con*2],))
    t2.start()
    t3 = threading.Thread(target=down_img,args=(img_list[thread_con*2+1:thread_con*3],))
    t3.start()
    t4 = threading.Thread(target=down_img,args=(img_list[thread_con*3+1:],))
    t4.start()


