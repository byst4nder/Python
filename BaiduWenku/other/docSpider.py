import re
import time
import json

import requests

from BaiduWenku.utils.log import log
from BaiduWenku.base.spider.BaseSpider import wenkuBaseSpider
from BaiduWenku.utils.http import HttpHeader
from BaiduWenku.setting import TIME_WITE
from BaiduWenku.base.db.file_doc import FileSave,filesave


class docSpider(wenkuBaseSpider):
    page_url = {}

    def __init__(self,url):
        super(docSpider, self).__init__(url=url)



    def get_page_url(self, resp):

        page = resp.content.decode('gbk')
        self.page_url = {x : y.replace('\\', '').replace('//wk/','/wk/') for x, y in
                    re.findall(r'[,\[]{.{10,30}:(\d{1,3}).{10,30}(https:.*?\.json\?.*?token.*?)\\x22}', page )}
        log.info('文档ID：%s，完成下载网址获取，共%s个链接。' % (self.docId, self.page_url.__len__()))


    def down_page(self,url):

        resp = self.get_page_base(url,HttpHeader.PageHeader())

        json_data = re.search('{.*}',resp.content.decode('unicode_escape', 'ignore')).group(0)

        da = json.loads(json_data)['body']
        da_j = ''
        for i in da:
            # print('1',type(i),type(i['c']),i['c'])
            if type(i['c']) == str:
                da_j += i['c'].strip()
        # 调用 filesave 实例处理文档内容保存
        filesave.Save(da_j,self.document)


    def run_down(self):
        for pageNum,url in self.page_url.items():
            log.info('正在下载文档（%s）第%s页，url：%s' % (self.docId, pageNum,url))
            self.down_page(url)
            log.info('文档（%s）第%s页下载完成，url：%s' % (self.docId, pageNum, url))
            time.sleep(TIME_WITE)

if __name__ == '__main__':


    # url = 'https://wenku.baidu.com/view/c55db74626d3240c844769eae009581b6bd9bd1d.html'
    url = r'https://wenku.baidu.com/view/8c3acd03ff4733687e21af45b307e87101f6f820.html'
    # url = 'https://wenku.baidu.com/view/8c8d30a9bb0d4a7302768e9951e79b8968026891.html?from=search'
    # url = 'https://wenku.baidu.com/view/f22deb61d1f34693dbef3e8b.html?from=search'
    docm = docSpider(url)
    docm.get_doc_info()
    docm.run_down()
    for x,y in docm.document.__dict__.items():
        print(x,':',y)
    log.info(url+' 下载完成')

