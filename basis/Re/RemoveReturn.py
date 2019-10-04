# !python3
# Remove text carriage return
# 自动替换粘贴板文本内容中的换行符。


import re
import pyperclip
import time

# TODO:换行符
textReturn = re.compile(r'[\r|\n]')  #\s{2,}    \r{0,1}\n{0,1}
# textReturn = re.compile(r'[\r|\n|\s]')  #\s{2,}    \r{0,1}\n{0,1}
temptext = ''    
recenttext = ''

while True:
    # TODO:在粘贴板中替换文本中的换行符
    temptext = str(pyperclip.paste())
    if temptext != recenttext:
        
        matches = textReturn.sub('',temptext)
 
        # TODO:将替换后的字符复制到粘贴板

        pyperclip.copy(matches)
        recenttext = pyperclip.paste()
        print(recenttext)
    time.sleep(0.2)