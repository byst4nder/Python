# ! python
# 打开文件夹中所有的文本（txt）文件，查找匹配用户提供的正则表达式的所有行。结果应该输出到屏幕上。


import re
import os
from pathlib import Path

def findLine(FolderPath:str,regex:str):

    fileRe= re.compile(r'.*\.((py)|(txt))')
    fileNameList=os.listdir(FolderPath)
    lineRe= re.compile(regex)
    linList=[]

    #TODO:查找指定文件夹中的txt文件

    FindFileNamd=[]
    for filename in fileNameList:
        findFile=fileRe.search(filename)
        if  findFile :
            FindFileNamd += [findFile.group()]

    #TODO:打开txt文件，读取每一行，并根据正则表达式进行匹配，

    for filename in FindFileNamd:
        filename= os.path.join(FolderPath,filename)
        fr=open(filename,'r',encoding='utf-8')
        for line in fr:
            lin=lineRe.search(line)
            if lin:
                linList += [lin.group()]
        fr.close()
    return linList





if __name__ == "__main__":

    restr = r'.*counts*'
    filepath=os.getcwd()
    linList=findLine(r'Q:\file',restr)
    for i in linList:
        print(i)


