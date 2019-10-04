# _*_ coding:utf-8 _*_
#! python3
# EMR日志处理

import re
import os
import sys

# groupRg = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<sip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<csmethod>\w{2,5}) (?P<csuristem>/[.\[\]/_\-a-zA-Z0-9]+\.\w{1,5}) (?P<csuristem2>((?P<id>\w{2,8}=(\d{5,8})*)&{0,3}\w{2,5}=(\d{4}-\d{2}-\d{2})*)|(\w{4,10}=(\d{4}.\d{0,2}.\d{0,2}.\d{0,5})|(\w{4,9}=(\d{1,4},){1,5}\d{1,3}))|(-))* (?P<sport>\d{1,3}) - (?P<cip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ((\w{7}/\d.\d\+\(.*\))|(\w{6}-.*\(.*\)))* (\w{4}:.*\?.*((-\d{2})|(=))*)*-* (\d{1,3}) (\d{1,3}) (\d{1,3}) (\d{1,3})')
groupRg = re.compile(
    r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<sip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<csmethod>\w{2,5}) (?P<csuristem>/[.\[\]a-zA-Z0-9/_-]+\.\w{1,5}) (?P<csuristem2>((?P<id>\w{2,8}=(\d{5,8})*)&{0,3}\w{2,5}=(\d{4}-\d{2}-\d{2})*)|(\w{4,10}=(\d{4}.\d{0,2}.\d{0,2}.\d{0,5})|(\w{4,9}=(\d{1,4},){1,5}\d{1,3}))|(-))* (?P<sport>\d{1,3}) - (?P<cip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<csUserAgent>(\w{7}/\d.\d\+\(.*\))|(\w{6}-.*\(.*\)))* (\w{4}:.*\?.*((-\d{2})|(=))*)*-* (?P<csStatus>\d{1,3}) (\d{1,3}) (\d{1,3}) (?P<timetaken>\d{1,3})')
# filepath=r'.\file\u_ex190721.log'

fileml = r'D:\python\W3SVC1'
totleline = 0
totlerror = 0

for fllog in os.listdir(fileml):
    filepath = os.path.join(fileml, fllog)
    emrfile = open(filepath, 'r', encoding='gb18030', errors='ignore')  #
    emrlog = open(r'.\file\emrlog.log', 'a', encoding='gb18030')
    emrerror = open(r'.\file\emrerror.log', 'a', encoding='gb18030')
    i = 0
    y = 0
    for fl in emrfile:
        grpMatch = groupRg.search(fl)
        i += 1
        totleline += 1
        if grpMatch:
            # print('{}--{}--{}--{}'.format(i,grpMatch.group('date'),grpMatch.group('time'),grpMatch.group('sip')))
            emrlog.write('{}--{}--{}--{}--{}\n'.format(fllog, i,
                                                       grpMatch.group('date'), grpMatch.group('time'), grpMatch.group('sip')))

        else:
            emrerror.write('{}--{}--{}'.format(fllog, i, fl))
            y += 1
            totlerror += 1
    emrfile.close()
    emrlog.close()
    emrerror.close()
    print('文件名:',fllog,'错误行：', y, '文件所有行：', i)
print('错误行：', totlerror, '所有行:', totleline)
