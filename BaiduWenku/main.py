
from BaiduWenku.base.spider.BaseSpider import wenkuBaseSpider
# bug vip共享文档 txt 未能下载内容 待修复
if __name__ == '__main__':
    url = input('请输入文库网址：')
    docm = wenkuBaseSpider(url)
    docm.run()


