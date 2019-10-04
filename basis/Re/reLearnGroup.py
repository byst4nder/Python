#! python3
# 正则表达式分组练习  提取分组内容


import re
import os

text='JPEG (jpg) FFD8FF'
groupRg = re.compile(r'(?P<a>.*) (?P<b>\(.*\)) (?P<c>.*)')
# groupRg = re.compile(r'(.*) (\(.*\)) (.*)')

filepath='./file/retext.txt'
file = open(filepath,'r',encoding='utf-8')

for fl in file:
    grpMatch=groupRg.search(fl)
    if grpMatch:
        print('{}--{}--{}'.format(grpMatch.group('a'),grpMatch.group('b'),grpMatch.group('c')))
        print(grpMatch.group(0))


