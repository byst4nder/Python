import re
import time
import json

from BaiduWenku.utils.log import log
from BaiduWenku.utils.http import HttpHeader
from BaiduWenku.setting import TIME_WITE
from BaiduWenku.base.db.file_doc import filesave
from BaiduWenku.base.spider.GetPageBase import get_page_base


class docSpider():
    page_url = {}

    def __init__(self,doc):
        self.document = doc

    # 获取文档内容网址
    def get_page_url(self, resp):

        page = resp.content.decode('gbk')
        self.page_url = {x : y.replace('\\', '').replace('//wk/','/wk/') for x, y in
                    re.findall(r'[,\[]{.{10,30}:(\d{1,3}).{10,30}(https:.*?\.json\?.*?token.*?)\\x22}', page )}
        log.info('文档ID：%s，完成下载网址获取，共%s个链接。' % (self.document.id, self.page_url.__len__()))

    # 下载文档内容
    def down_page(self,url):

        resp = get_page_base(url,HttpHeader.PageHeader())

        json_data = re.search('{.*}',resp.content.decode('unicode_escape', 'ignore')).group(0)

        da = json.loads(json_data)['body']
        da_j = ''
        for i in da:
            # print('1',type(i),type(i['c']),i['c'])
            if type(i['c']) == str:
                da_j += i['c'].strip()
        # 调用 filesave 实例处理文档内容保存
        filesave.Save(da_j,self.document)

    # 控制文档下载
    def run_down(self,resp):
        self.get_page_url(resp)
        for pageNum,url in self.page_url.items():
            log.info('正在下载文档（%s）第%s页，url：%s' % (self.document.id, pageNum,url))
            self.down_page(url)
            log.info('文档（%s）第%s页下载完成，url：%s' % (self.document.id, pageNum, url))
            time.sleep(TIME_WITE)



