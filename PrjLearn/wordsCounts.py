# encoding:utf-8
# 词频率统计 涉及文件打开、写入，字符串处理
# 2019-08-12
from pathlib import Path
import os
import fileinput
import string

# 设置文件相对路径或绝对路径
# filepath = 'TabularSSAS.txt'  #'DAX.txt'
# filepath = 'The_Definitive_Guide_to_DAX_Alberto_Ferrari.txt'
pathlist = ['TabularSSAS.txt','DAX.txt','The_Definitive_Guide_to_DAX_Alberto_Ferrari.txt','LearntoWriteDAX.txt']
# p = Path('.')
# 打开文件 r为只读
words = []
for filepath in pathlist:
    fo = open(filepath, 'r', encoding='utf-8')

    # 读入文本内容，并分割为单词，转换为列表
    words += [s.strip(string.punctuation).lower()
            for s in fo.read().split()]
    # 关闭文件
    fo.close()

# 通过set集合去掉单词里面的重复项，建立字典key
key = set(words)
# 生成key为单词，value值为频率的字典
words_disc = {s: words.count(s) for s in key}

# 打开文件 w为覆盖写入
filepath = 'words.txt'
fo = open(filepath, 'w', encoding='utf-8')

# 按照value值对key关键字排序，返回一个key关键字列表
word_disc_sort=sorted(words_disc, key=lambda x: words_disc[x], reverse=True)
# 根据排序后的列表，输出单词及频率
for word in word_disc_sort:
    # print('{}--{}times'.format(word, words_disc[word]))
    fo.write('{}--{}times\n'.format(word, words_disc[word]))
# 关闭文件
fo.close
