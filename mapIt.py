#! python3
# webbrowser 模块练习
# 
import webbrowser
import sys
import pyperclip

# webbrowser 属性和方法练习
# webbrowser.open_new("http://inventwithpython.com/")
# print(webbrowser.__file__)
# print(webbrowser.__doc__)
# print(webbrowser._browsers)
# print(webbrowser._tryorder)

if len(sys.argv)>1:
    searchstr = ' '.join(sys.argv[1:])
else:
    searchstr = pyperclip.paste()
webbrowser.open('{}{}'.format("https://www.baidu.com/s?wd=",searchstr))   
webbrowser.open('{}{}'.format(r"https://map.baidu.com/search?querytype=s&da_src=shareurl&wd=",searchstr)) 


