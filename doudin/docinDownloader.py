import re
import os
# import common
from doudin.docinParse import createDir
import doudin.docinParse

reg_getDocinPageID = re.compile("http://www\.docin\.com/p-(\d+)\.htm")


def getPageID(url):
    try:
        return reg_getDocinPageID.findall(url)[0]
    except:
        return None

def getTitle(url):
    pass

def urlDownloadToFile(url,filename):
    pass

class docinDownloader():
    def __init__(self):
        pass

    def download(self, url, savePath="./tmpDocin"):
        createDir(savePath)
        self._pageID = getPageID(url)
        self._title = getTitle(url).replace(" - 豆丁网", "")
        for i in range(1, 100):  # 具体也不知道会有多少个文件, 所以只能一个个判断。。
            filename = "{0}/{1}_{2}.docin".format(savePath, self._title, i)
            if (i == 1):
                urlDownloadToFile("http://221.122.117.125/docin_{0}.docin".format(self._pageID), filename)
            else:
                urlDownloadToFile("http://221.122.117.125/docin_{0}_{1}.docin".format(self._pageID, i),
                                         filename)
            # 测试了一下。。发现如果请求的文件不存在则会返回一个包含ERROR字符的文档或者空文档。。
            # 所以这里的1024其实有点大。。。
            if (os.path.getsize(filename) < 1024):
                os.remove(filename)
                return


def main():
    downloader = docinDownloader()
    downloader.download("http://www.docin.com/p-760258140.html&ccid=100003")


if (__name__ == "__main__"):
    main()
