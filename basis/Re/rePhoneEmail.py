# python3
# 这是一个练习正则表达式的程序
# 先复制网页或其它文本，在运行本程序，自动提取邮箱和电话号码

import re
import pyperclip
import time

# TODO:电话号码正则表达式
phoneNumberRe = re.compile('''1[3-9]\d{9}''', re.IGNORECASE)
# TODO:邮箱正则表达式
emailRe = re.compile(
    '''[a-z0-9_\-]{3,}@[a-z0-9\-]*\.[a-z0-9]{2,3}''', re.IGNORECASE)

matches = []
temptext = ''    
recenttext = 'a'

while True:
    # TODO:在粘贴板中查找符合要求的电话号码和邮箱
    temptext = str(pyperclip.paste())
    if temptext != recenttext:
        
        phoneNum = phoneNumberRe.findall(temptext)
        email = emailRe.findall(temptext)

        # TODO:将匹配的电话号码和邮箱生成字符并复制到粘贴板
        matches = email + phoneNum
        if len(matches) > 0:
            pyperclip.copy('\n'.join(matches))
            recenttext = pyperclip.paste()
            print(recenttext)
        else:
            print('No phone numbers or email addresses found.')
            recenttext = temptext
    time.sleep(0.2)

