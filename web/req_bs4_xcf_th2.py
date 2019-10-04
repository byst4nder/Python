#! python
# 下载 下厨房网站首页图片
# 多线程

import os
import time
import struct
import lxml
from urllib.parse import urlparse
import requests
import threading
import bs4
from queue import Queue


class global_val():
    look_dir = 0

    def __init__(self):
        self.look_dir = 0

    @classmethod
    def bs_path(cls,path_name):
        cls.base_path=path_name


# 解析网页并将 url 加入到队列中
def check_url(url):

    # 打开网页，获取网页
    resp = requests.get(url)

    #  解析图片网址,并加入到队列中
    bs = bs4.BeautifulSoup(resp.text,'lxml')
    # open(os.path.join(bspath,'xcf.html'),'w',encoding='utf-8').write(bs.prettify())

    for img in bs.find_all('img'):
        pic_info = {}
        if img.has_attr('data-src'):
            imgurl = img.attrs['data-src']
        else:
            imgurl = img.attrs['src']

        o = urlparse(imgurl)
        pic_info['imgurl'] = '%s://%s%s' % (o.scheme, o.netloc, o.path.split('@')[0])
        pic_info['imgname'] = o.path.split('@')[0].split('/')[-1][1:]
        pic_info['imgpath'] = o.path.split('@')[0].replace('/','\\')[1:]
        # 将图片信息加入队列
        link_queue.put(pic_info)


# 下载img
def down_img(picurl:dict):
    print('%s 正在下载：%s:' % (threading.current_thread().name, picurl['imgurl']))
    picurl['data'] = requests.get(picurl['imgurl'])
    return  picurl

def Create_path(flpath):
    if os.path.isdir(os.path.dirname(flpath)):
        return True
    else:
        while True:

            if global_val.look_dir == 1:
                time.sleep(0.2)
                continue
            else:
                global_val.look_dir = 1
                os.mkdir(os.path.dirname(flpath))
                global_val.look_dir = 0
                break
        return True

# 将下载数据，保存到本地文件
def process_data(data):

    # 生成文件路径
    filepath = os.path.join(os.curdir, base_path,data['imgpath'])

    # 判断文件夹是否存在，不存在则创建文件夹
    Create_path(filepath)

    # 将图片信息写入文件
    with open(filepath, 'wb') as f:
        for chunk in data['data'].iter_content(1024):
            f.write(chunk)
    print('%s 保存在 %s.' % (data['imgname'],filepath))


# 线程启动，从队列获取信息后并处理
def download():
    i = 0
    while True:
        # 阻塞直到从队列获取一条消息
        link = link_queue.get()
        i += 1
        # 判断是否收到队列完成信号
        if link is None:
            break
        # 下载图片
        data = down_img(link)
        # 处理数据
        process_data(data)
        # 给队列返回完成消息
        link_queue.task_done()
        print('remaiing queue:%dS' % link_queue.qsize())




if __name__ == '__main__':
    start_time = time.time()
    # 文件夹锁
    # global_val.look_dir = 0

    # 线程队列
    threads = []
    # 线程梳理
    threads_num = 50
    # 基础文件夹
    base_path = 'img'

    url = 'http://www.xiachufang.com/'
    url = 'https://www.xiachufang.com/category/40076/'
    link_queue = Queue()

    # 解析下厨房网站地址，并将图片地址加入队列中
    # for i in range(1,11):
    #     url='https://www.xiachufang.com/category/40076/?page=%s' % i

    check_url(url)

    # 启动线程下载并保存图片，并将线程对象放入一个列表
    for i in range(threads_num):
        t = threading.Thread(target=download)
        threads.append(t)
        t.start()

    # 阻塞队列，直到队列被清空
    link_queue.join()

    # 向线程发生退出信号 None（可以自定义）
    for i in range(threads_num):
        link_queue.put(None)

    # 阻塞线程，等待线程退出
    for t in threads:
        t.join()
    totle_time = time.time()-start_time
    print('下载完成用时：',totle_time)



