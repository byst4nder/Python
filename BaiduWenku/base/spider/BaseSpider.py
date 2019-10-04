'''
    从给定网址采集文档信息
    。给定关键字搜索百度文库，根据文档类型获取文档url
    。根据文档URL获取文档基本信息，以及文档数据url
    。根据数据url下载文档内容，对数据进行清洗、组合成文档。
'''

import re
import json
from urllib import parse

from bs4 import BeautifulSoup

from BaiduWenku.utils.http import HttpHeader
from BaiduWenku.document import Document
from BaiduWenku.utils.log import log
from BaiduWenku.base.spider.GetPageBase import get_page_base
from BaiduWenku.base.spider.docSpider import docSpider
from BaiduWenku.base.spider.txtSpider import txtSpider
from BaiduWenku.base.db.file_doc import filesave



class wenkuBaseSpider():

    WkInfo_docType = {
        '0': None,
        '1': docSpider,
        '2': None,
        '3': None,
        '4': docSpider,
        '5': None,
        '6': None,
        '7': None,
        '8': txtSpider,
        '9': None,
        '10': None,
        '11': None,
        '12': None,
        '13': None,
        '14': None,
        '15': None,
        '16': None
    }

    def __init__(self,url):
        # 获取文档URL
        self.url = url
        # 获取文档ID
        self.docId = re.search(r'.*?wenku\.baidu\.com/view/(\w+?)\.html?.*',url).group(1)
        # 生成文档类
        self.document = Document(id=self.docId,url=self.url)


    # 获取文档下载量、评分等网址
    def _get_score_url(self):
        return 'https://wenku.baidu.com/doc/interface/docCount?viewCountIncr=1&doc_id={}&sl=0'.format(self.docId)

    # 获取文档下载量、评分等
    def _get_score(self):

        resp = get_page_base(self._get_score_url())
        cont = resp.content.decode('gbk')
        # 将json内容转为字典
        getscore = json.loads(cont)
        # qualityScore: 文档评分
        self.document.qualityScore = getscore['qualityScore']
        # viewCount：阅读量
        self.document.viewCount = getscore['viewCount']
        # percentage: 高于其他文档百分比
        self.document.percentage = getscore['percentage']
        # downloadCount：下载量
        self.document.downloadCount = getscore['downloadCount']
        # print(getscore)


    # 获取文档信息
    def get_doc_info(self):

        # 获取URL html信息
        self.resp = get_page_base(self.url,headers=HttpHeader.LoginHeader())
        # resp = self.r.get(url = self.url,headers=self.loginheader)

        # html 编码装潢
        cont = self.resp.content.decode('gbk')

        # 获取文档标题/类型/页数等信息
        soup = BeautifulSoup(cont,'lxml')

        # title: 文档标题
        self.document.title = re.search('\'title\'.*?\'(.*?)\'',cont).group(1)
        # creater: 文档上传者
        self.document.creater = parse.unquote(re.search('\'creater\'.*?\'(.*?)\'',cont).group(1),'gbk')
        # docType: 文档格式（类型）
        self.document.docType = re.search('\'docType\'.*?\'(.*?)\'',cont).group(1)
        # docTypeNum: 文档格式号（类型）
        self.document.docTypeNum = re.search('\'docTypeNum\'.*?\'(.*?)\'',cont).group(1)
        # totalPageNum: 文档总页数
        self.document.totalPageNum = re.search('\'totalPageNum\'.*?\'(.*?)\'',cont).group(1)
        # freepagenum：免费阅读页数
        self.document.freepagenum = re.search('\'freepagenum\'.*?\'(.*?)\'',cont).group(1)
        # put_date: 文档上传日期 '//*[@id="doc-header-test"]/div/span/em'
        self.document.put_date = soup.find(id="doc-header-test").find('em').get_text()

        # payPrice: 文档价格
        self.document.payPrice = re.search('\'payPrice\'.*?\'(.*?)\'',cont).group(1)
        # downloadCoupons: 下载劵
        self.document.downloadCoupons = ''
        # isPaymentDoc：是否为付费文档
        self.document.isPaymentDoc = re.search('\'isPaymentDoc\'.*?\'(.*?)\'',cont).group(1)

        # content 文档内容
        self.document.conetent = ''
        # 获取文档评分
        self._get_score()
        self._documentSave()

        # print(self.document.__dict__)
        return self.document

    def _documentSave(self):
        for x,y in self.document.__dict__.items():
            filesave.Save('%s:%s\n' % (x,y),self.document)

    def run(self):
        self.get_doc_info()
        log.info('你下载的文档ID为：%s,文档标题为：%s,文档类型为：%s' % (self.document.id,self.document.title,self.document.docType))
        ws = self.WkInfo_docType[self.document.docTypeNum]
        if ws:
            pag = ws(self.document)
            pag.run_down(self.resp)
        else:
            log.info('你的文档类型不支持下载，文档类型为：%s' % self.document.docType)



