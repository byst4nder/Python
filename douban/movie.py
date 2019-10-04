#! python3
# 这个是下载豆瓣电影分类排行榜 - 喜剧片

import os
import time
import re
import lxml
# from lxml import etree
import json
import requests
from queue import Queue
from urllib.parse import urlparse
from threading import Thread
from bs4 import  BeautifulSoup



class glob_value():
    cover_queues = Queue()
    url_queues = Queue()
    img_path = 'imgs'
    look_dir = 0
    queues_cover_num = 50
    queues_url_num = 20
    file_path = 'file'
    header = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://movie.douban.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

def Create_path(flpath):
    if os.path.isdir(os.path.dirname(flpath)):
        return True
    else:
        while True:
            if glob_value.look_dir == 1:
                time.sleep(0.2)
                continue
            else:
                glob_value.look_dir = 1
                os.makedirs(os.path.dirname(flpath))
                glob_value.look_dir = 0
                print('系统已经创建目录：', flpath)
                break
        return True


def get_rank(url):

    movie_list = []
    r = requests.get(url,headers=glob_value.header,verify=False)
    if int(r.status_code) == 200 and r.text:
        movie_list = json.loads(r.text)
        for m in movie_list:
            cover_list = {}
            cover_list['id'] = m['id']
            cover_list['cover_url'] = m['cover_url']
            cover_list['path'] = urlparse(m['cover_url']).path[1:].replace('/','\\')
            glob_value.cover_queues.put(cover_list)

            url_list = {}
            url_list['id'] = m['id']
            url_list['url'] = m['url']
            glob_value.url_queues.put(url_list)
            print(url_list)
    else:
        print('m is none')
    return movie_list

def cover_down(cover_url):
    r = requests.get(cover_url['cover_url'],headers=glob_value.header,verify=False)
    filename = os.path.join(os.curdir,glob_value.img_path,cover_url['path'])
    # print('img save fl:',filename)
    Create_path(filename)
    with open(filename,'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)


# 提取每个电影的评论
def movie_down(movie_url):
    # 'Accept': '*/*',
    # movie_url = 'https://movie.douban.com/subject/1301445/comments?start=20&limit=20&sort=new_score&status=P'
    hearder_movie = {
        "Connection": "keep-alive",
        'X-Requested-With': 'XMLHttpRequest',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": '',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    print('%s**************************'% str(movie_url['id']))
    data_file_name = os.path.join(os.curdir, glob_value.file_path, 'data.txt')
    requests_movie = requests.session()
    i = 0
    for i in range(0,201,20):
        movie_page_list = []
        # url = 'https://movie.douban.com/subject/1301445/comments?start=%s&limit=20&sort=new_score&status=P' % i
        url = '%scomments?start=%s&limit=20&sort=new_score&status=P' % (movie_url['url'],i)
        if i == 0:
            # ref_url = 'https://movie.douban.com/subject/1301445/'
            ref_url = movie_url['url']
        else:
            # ref_url = 'https://movie.douban.com/subject/1301445/comments?start=%s&limit=20&sort=new_score&status=P' % str(i-20)
            ref_url = '%scomments?start=%s&limit=20&sort=new_score&status=P' % (movie_url['url'],str(i-20))
        hearder_movie['Referer'] = ref_url
        r = requests_movie.get(url,headers=hearder_movie,verify=False)
        if int(r.status_code) == 200 and r.text:
            filename = os.path.join(os.curdir,glob_value.file_path,'%s.txt' % i)
            Create_path(filename)
            with open(filename, 'w' ,encoding='utf-8') as f:
                f.write(r.text)

            page = lxml.etree.HTML(r.text)

            a = page.xpath('//*[@id="comments"]/div/div[2]')
            for m in a:
                ls = {}
                ls['id'] = movie_url['id']
                ls['author'] = m.xpath('.//h3/span[2]/a/text()')[0].split()
                ls['date'] = m.xpath('.//span[@class="comment-time "]/text()')[0].split()
                ls['comment']  = m.xpath('.//p/span/text()')[0].split()
                # movie_page_list.append(ls)
                s = ''
                for x,y in ls.items():
                    print('提取信息>>%s:%s;' % (x,y))
                    s += '%s:%s;' % (x,y)
                with open(data_file_name, 'a', encoding='utf-8') as f:
                    f.write('%s\n' %s)

            return movie_page_list





# 下载图片队列管理
def queues_cover():
    while True:
        link_cover = glob_value.cover_queues.get()
        print('队列剩余数量：%dS' % glob_value.cover_queues.qsize())
        # print(link_cover)
        if link_cover is None:
            break
        cover_down(link_cover)
        glob_value.cover_queues.task_done()
        # print('ID:{},已经下载完成。'.format(link_cover['id']))

# 下载评论队列管理
def queues_url():
    while True:
        link_url = glob_value.url_queues.get()
        # print(link_url)
        if link_url is None:
            break
        movie_down(link_url)
        glob_value.url_queues.task_done()

if __name__ == '__main__':


    url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=500'

    # 电影评论页
    # movie_url = 'https://movie.douban.com/subject/1301445/comments?status=P'
    # 'https://movie.douban.com/subject/1301445/comments?start=20&limit=20&sort=new_score&status=P'

    queues_cover_thread = []
    for i in range(glob_value.queues_cover_num):
        t = Thread(target=queues_cover)
        t.start()
        queues_cover_thread.append(t)

    queues_url_thread = []
    for i in range(glob_value.queues_url_num):
        t = Thread(target=queues_url)
        t.start()
        queues_url_thread.append(t)




    movie_list = get_rank(url)

    mo_name = os.path.join(os.curdir,glob_value.file_path,'movie.txt')
    Create_path(mo_name)


    # 保存电影列表内容
    m= {}
    with open(mo_name,'a',encoding='utf-8') as f:
        for m in movie_list:
            s = ''
            for x,y in m.items():
                s += '%s:%s;'%(x,y)
            f.write(s+'\n')
    glob_value.cover_queues.join()


    for i in range(glob_value.queues_cover_num):
        glob_value.cover_queues.put(None)

    for t in queues_cover_thread:
        t.join()

    for i in range(glob_value.queues_url_num):
        glob_value.url_queues.put(None)

    for t in queues_url_thread:
        t.join()



