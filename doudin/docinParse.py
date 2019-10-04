"""
    参考:
        http://blog.csdn.net/lin379184514/article/details/5305061  #mfc版本
        http://blog.csdn.net/kowity/article/details/6342925        #python版本(主要参考)
        http://blog.sina.com.cn/s/blog_6859df370100wsv2.html       #swf文件格式
        http://blog.csdn.net/jgood/article/details/4608546         #zlib用法
"""

# 原文链接：https: // blog.csdn.net / qq506657335 / article / details / 20006273


import urllib
import re
import os
import struct
import zlib
# import common

reg_getDocinPageID = re.compile("http://www\.docin\.com/p-(\d+)\.htm")
reg_getDocTitle = re.compile('')

def getDocinDocInfo(url):
    docID = reg_getDocinPageID.findall(url)[0]
    docName = reg_getDocTitle.findall(urllib.request.urlopen(url).read().decode())[0]
    return docID, docName

def createDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

class docinParse():
    def __init__(self):
        # 这几个数值参考:http://blog.sina.com.cn/s/blog_6859df370100wsv2.html
        self._swfCommon = struct.pack('bbbb', 0x46, 0x57, 0x53, 9)

    def _getSwfInfo(self, docinFile):
        self._swfWidth = struct.unpack("i", docinFile.read(4))[0]  # 获取swf文件的宽度
        self._swfHeight = struct.unpack("i", docinFile.read(4))[0]  # 获取swf文件的高度
        self._swfPages = struct.unpack("i", docinFile.read(4))[0]  # 获取swf文件的页度
        self._swfHeaderLength = struct.unpack("i", docinFile.read(4))[0]  # 获取swf文件头的长度



    def parse(self, filename, startIndex=1, savePath="tmpSwf"):
        createDir(os.path.join(os.curdir,savePath))
        docinFile = open(filename, "rb")
        self._getSwfInfo(docinFile)

        swfHeader = zlib.decompress(docinFile.read(self._swfHeaderLength))

        for page in range(startIndex, startIndex + self._swfPages):
            byteBodyLen = docinFile.read(4)
            """
                文档若是超过50页, 
                则会被分成N部分, 
                每部分50页,(一个文件最多只有50页)
                所以需要判断是否为空.
            """
            if (byteBodyLen == b""):
                return
            bodyLen = struct.unpack("i", byteBodyLen)[0]
            swfBody = zlib.decompress(docinFile.read(bodyLen))
            swf = swfHeader + swfBody

            file = open("{0}/{1}.swf".format(savePath, page), "wb")
            file.write(self._swfCommon + struct.pack("i", len(swf)) + swf)
            file.close()





if __name__ == '__main__':
    docinParser = docinParse()
    docinParser.parse("page_913760031_2.swf")

