#! python3
# 文档的数据模型，封装文档的相关信息，比如文档标题、作者、阅读量、文档类型等。

class Document(object):

    # 1.初始化文档类型
    def __init__(self, id, url, title='', creater=None, put_date=None, docType=0, docTypeNum=-1, totalPageNum=-1,
                 qualityScore=-1, percentage=None, payPrice=None, downloadCoupons=None, isPaymentDoc=None,
                 freepagenum=None, viewCount=None, downloadCount=None, conetent=None):
        """
        :param id: 文档Id
        :param url: 文档URL
        :param title: 文档标题
        :param creater: 文档上传者
        :param put_date: 文档上传日期
        :param docType: 文档格式（类型）
        :param docTypeNum: 文档格式号（类型）
        :param totalPageNum: 文档总页数
        :param qualityScore: 文档评分
        :param percentage: 高于其他文档百分比
        :param payPrice: 文档价格
        :param downloadCoupons: 下载劵
        :param isPaymentDoc: 是否为付费文档
        :param freepagenum: 免费阅读页数
        :param viewCount: 阅读量
        :param downloadCount: 下载量
        :param conetent: 文档内容
        """
        # docId：文档Id
        self.id = id
        # title: 文档标题
        self.title = title
        # creater: 文档上传者
        self.creater = creater
        # put_date: 文档上传日期
        self.put_date = put_date
        # docType: 文档格式（类型）
        self.docType = docType
        # docTypeNum: 文档格式号（类型）
        self.docTypeNum = docTypeNum
        # totalPageNum: 文档总页数
        self.totalPageNum = totalPageNum
        # qualityScore: 文档评分
        self.qualityScore = qualityScore
        # percentage: 高于其他文档百分比
        self.percentage = percentage
        # payPrice: 文档价格
        self.payPrice = payPrice
        # downloadCoupons: 下载劵
        self.downloadCoupons = downloadCoupons
        # isPaymentDoc：是否为付费文档
        self.isPaymentDoc = isPaymentDoc
        # freepagenum：免费阅读页数
        self.freepagenum = freepagenum
        # viewCount：阅读量
        self.viewCount = viewCount
        # downloadCount：下载量
        self.downloadCount = downloadCount
        # content 文档内容
        self.conetent = conetent
        self.url = url
        # 文档类型字典
        # self.WkInfo_docType = {
        #     '0': '',
        #     '1': 'doc',
        #     '2': 'xls',
        #     '3': 'ppt',
        #     '4': 'docx',
        #     '5': 'xlsx',
        #     '6': 'pptx',
        #     '7': 'pdf',
        #     '8': 'txt',
        #     '9': 'wps',
        #     '10': 'et',
        #     '11': 'dps',
        #     '12': 'vsd',
        #     '13': 'rtf',
        #     '14': 'pot',
        #     '15': 'pps',
        #     '16': 'epub'
        # }
