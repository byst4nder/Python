import re
import json

from BaiduWenku.utils.log import log
from BaiduWenku.utils.http import HttpHeader
from BaiduWenku.base.db.file_doc import filesave
from BaiduWenku.base.spider.GetPageBase import get_page_base


class txtSpider():

    page_url = {}

    def __init__(self,doc):
        self.document = doc

    def get_page_url(self,page):
        getdocinfo_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=%s' % self.document.id

        resp = get_page_base(getdocinfo_url,HttpHeader.LoginHeader())

        content = resp.content.decode('utf-8')

        # 获取文档内容url参数
        md5 = re.findall('"md5sum":"(.*?)"',content)[0]
        pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
        rsign = re.findall('"rsign":"(.*?)"', content)[0]
        # 合成url
        content_url = 'https://wkretype.bdimg.com/retype/text/' + self.document.id + '?rn=' + pn + '&type=txt' + md5 + '&rsign=' + rsign
        self.page_url = {'1': content_url}
        log.info('文档ID(%s)下载网址获取完成，url:%s。' % (self.document.id, content_url))

    def down_page(self,url):

        resp = get_page_base(url, HttpHeader.TextHeader())

        cont = resp.content.decode('unicode_escape', 'ignore').replace('\r\n','')

        datas = re.findall('{"c":"(.*?)".*?"}.*?(\d+).*?\d+}', cont)

        for data,index in datas:
            # 调用 filesave 实例处理文档内容保存
            filesave.Save(data, self.document)
            log.info('文档（%s）正在写入第%s页' % (self.document.id, index))

    def run_down(self,resp):
        self.get_page_url(resp)
        # filesave.Save(json.dumps(self.document.__dict__,ensure_ascii=False),self.document)
        log.info('文档（%s）正在下载，url：%s' % (self.document.id, self.page_url['1'] ))
        self.down_page(self.page_url['1'])
        log.info('文档（%s）下载完成，url：%s' % (self.document.id, self.page_url['1']))

