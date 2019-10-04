#! python3
# 练习webdriver方法、属性练习
#
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import bs4
import time
import pickle
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
import  json

# 设置chrome浏览器界面模式
# 驱动executable_path=r'D:\pythondrive\chromedriver.exe',
def ChromeDriverBrowser(web_header = True):

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    # 判断是否返回有界面浏览器
    if web_header:
        driverChrome = webdriver.Chrome()
        return driverChrome

    # 浏览器参数设置
    chrome_options = Options()
    chrome_options.add_argument('--headless')               #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('window-size=1920x3000')    # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')            #谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars')        #隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
    chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" #手动指定使用的浏览器位置
    # chrome_options.add_argument(headers)
    driverChrome = webdriver.Chrome(options=chrome_options)
    return driverChrome

    # 创建chrome参数对象
    # opt = webdriver.ChromeOptions()
    # # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    # opt.headless = True
    # driverChrome = webdriver.Chrome(options=opt)
    # return driverChrome


# 登录OA系统,获取cookie,并保存问文件,返回登录主页page
def oa_login(url):

    # 调用浏览器
    browser = ChromeDriverBrowser(False)

    # 打开网页
    browser.get(url)

    # 登录页面写入文件 测试用
    open(r'.\file\oalogin.txt', 'w', encoding='utf-8').write(browser.page_source)

    # 模拟登录
    browser.find_element_by_id('loginid').send_keys('61309011')
    browser.find_element_by_id('userpassword').send_keys('wl123456')
    browser.find_element_by_id('login').submit()

    # 将cookies写入文件
    pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))
    page = browser.page_source
    brower_close(browser)
    return page

# 通过cookie访问url，并返回html文件
def cookie_browse(oa_url):
    cok_bro=ChromeDriverBrowser(False)
    cok_bro.get(oa_url)
    # cok_bro.delete_cookie()
    cok_bro.delete_all_cookies()
    cookies = pickle.load(open('cookies.pkl', 'rb'))
    for cookie in cookies:
        cok_bro.add_cookie({
            "domain": cookie.get('domain'),
            'httpOnly': cookie.get('httpOnly'),
            'name': cookie.get('name'),
            'path': cookie.get('path'),
            'secure': cookie.get('secure'),
            'value': cookie.get('value'),
        })
    cok_bro.get(oa_url)
    page_source=cok_bro.page_source
    time.sleep(0.3)
    brower_close(cok_bro)
    return page_source


# 解析main主页网页,返回url，返回类型dict
def get_main_url(page):

    urllist = {}
    SourcePage = bs4.BeautifulSoup(page, 'html.parser')
    # 查找个人门户
    PersonalPortal = SourcePage.find_all(id='portal21')
    # 查找医院门户
    HospitalPortal = SourcePage.find_all(id="portal2")
    # 查找密码变更提醒和生日提醒
    urlother = SourcePage.select('[url]')
    # 将结果组合成字典
    if PersonalPortal:
        urllist['Personal'] = '{}{}'.format(url, PersonalPortal[0].get('href'))
    if HospitalPortal:
        urllist['Hospital'] = '{}{}'.format(url, HospitalPortal[0].get('href'))
    if urlother:
        urllist['other1'] = '{}{}'.format(url,urlother[0].get('url'))
        urllist['other2'] = '{}{}'.format(url,urlother[1].get('url'))

    return urllist



# 关闭浏览器
def brower_close(browser):
    browser.close()


if __name__ == '__main__':

    # 定义OA网址
    url = 'http://oa.cqszfy.com:10000'

    # 模拟登录系统，保存cookie为cookies.pkl
    oa_soruce = oa_login(url)
    open(r'.\file\oa\{}.txt'.format('main'),'w',encoding='utf-8').write(oa_soruce)
    # open(r'.\file\oamin.txt', 'w', encoding='utf-8').write(oa_soruce)
    # 解析main主页，获取医院门户、个人门户等网址
    url_main = get_main_url(oa_soruce)
    #  测试打开 网页

    for x,y in url_main.items():
        print(x,y)
        open(r'.\file\oa\{}.txt'.format(x), 'w', encoding='utf-8').write(cookie_browse(y))
