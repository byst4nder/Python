import os
import time

from BaiduWenku.utils.log import log
'''
    2）文档存储模块
        把下载的文档数据保存到数据库或者指定位置
'''

class FileSave():


    def __init__(self,savepath = 'file'):
        self.fp = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),savepath)
        print('文件目录',self.fp)
        self.make_path()

    def base_path(self):
        os.path.pardir()

    def make_path(self):
        if not os.path.isdir(self.fp):
            os.makedirs(self.fp)
            log.info('创建目录%s' % self.fp)


    def Save(self,cont,document):
        filename = '%s/%s.txt' % (self.fp,document.title)

        with open(filename,'a',encoding='utf-8') as f:
            f.write(cont)


filesave = FileSave()

if __name__ == '__main__':
    FileSave()
    print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    print(os.path.abspath('..'))
    pass