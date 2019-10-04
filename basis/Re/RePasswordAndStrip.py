# !python3
# 正则表达式练习


import re

# 检测输入密码强调，强口令的定义是： 长度不少于 8 个字符， 同时包含大写和小写字符， 至少有一位数字。


def DetectionPassword(pwd: str):
    # 建立正则匹配模式
    pwdReCap = re.compile(r'[A-Z]+')
    pwdReLow = re.compile(r'[a-z]+')
    pwdNum = re.compile(r'\d+')
    pwdLen = re.compile(r'.{8,}')
    # 对输入pwd进行匹配

    detcCap = pwdReCap.search(pwd)
    detcLow = pwdReLow.search(pwd)
    detcNum = pwdNum.search(pwd)
    detcLen = pwdLen.search(pwd)
    # print(detcCap,detcLow,detcNum,detcLen)
    if detcLen and detcCap and detcLow and detcNum:
        return 1
    else:
        return 0


# strip() 实现该字符串函数的功能

def mystrip(string: str, restr=None):
    if string == None:
        return None
    x = 0
    y = len(string)-1
    if not restr:
        while string[x] == ' ' and x <= y:
            x += 1
        if x < y:
            while string[y] == ' ':
                y -= 1
        if x == y:
            return None
        else:
            return string[x:y+1]
    else:
        strRe = '[{}]'.format(restr)
        replaceRe = re.compile(strRe)
        return replaceRe.sub('',string)


if __name__ == "__main__":
    # password = input('请输入你待检测的密码：')
    # if(DetectionPassword(password)):
    #     print('你的密码通过了强调检查。')
    # else:
    #     print('密码强调不够。')

    teststr = input('请输入字符串:')
    print(teststr)
    teststr1 = mystrip(teststr, 'a-z')
    teststr2 = mystrip(teststr, ' ')
    print(teststr1)
    print(teststr2)
