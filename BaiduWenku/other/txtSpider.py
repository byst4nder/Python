import re
import json

from BaiduWenku.utils.log import log
from BaiduWenku.base.spider.BaseSpider import wenkuBaseSpider
from BaiduWenku.utils.http import HttpHeader
from BaiduWenku.base.db.file_doc import filesave


class txtSpider(wenkuBaseSpider):

    page_url = {}

    def __init__(self,url):
        super(txtSpider, self).__init__(url=url)

    def get_page_url(self,page):
        getdocinfo_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=%s' % self.docId

        resp = self.get_page_base(getdocinfo_url,HttpHeader.LoginHeader())

        content = resp.content.decode('utf-8')

        # 获取文档内容url参数
        md5 = re.findall('"md5sum":"(.*?)"',content)[0]
        pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
        rsign = re.findall('"rsign":"(.*?)"', content)[0]
        # 合成url
        content_url = 'https://wkretype.bdimg.com/retype/text/' + self.docId + '?rn=' + pn + '&type=txt' + md5 + '&rsign=' + rsign
        self.page_url = {'1': content_url}
        log.info('文档ID(%s)下载网址获取完成，url:%s。' % (self.docId, content_url))

    def down_page(self,url):

        resp = self.get_page_base(url, HttpHeader.TextHeader())

        cont = resp.content.decode('unicode_escape', 'ignore').replace('\r\n','')

        datas = re.findall('{"c":"(.*?)".*?"}.*?(\d+).*?\d+}', cont)

        for data,index in datas:
            # 调用 filesave 实例处理文档内容保存
            filesave.Save(data, self.document)
            log.info('文档（%s）正在写入第%s页' % (self.docId, index))

    def run_down(self):
        filesave.Save(json.dumps(self.document.__dict__,ensure_ascii=False),self.document)
        log.info('文档（%s）正在下载，url：%s' % (self.docId, self.page_url['1'] ))
        self.down_page(self.page_url['1'])
        log.info('文档（%s）下载完成，url：%s' % (self.docId, self.page_url['1']))



if __name__ == '__main__':


    # url = 'https://wenku.baidu.com/view/c55db74626d3240c844769eae009581b6bd9bd1d.html'
    # url = 'https://wenku.baidu.com/view/8c8d30a9bb0d4a7302768e9951e79b8968026891.html?from=search'
    # TXT
    url = 'https://wenku.baidu.com/view/f22deb61d1f34693dbef3e8b.html?from=search'
    docm = txtSpider(url)
    docm.get_doc_info()
    docm.run_down()
    for x,y in docm.document.__dict__.items():
        print(x,':',y)
    log.info(url+' 下载完成')


