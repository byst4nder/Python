# -*- coding:UTF-8 -*-

# 爬取百度doc txt 文档
#  https://wenku.baidu.com/view/c4bf72fdb5daa58da0116c175f0e7cd18525183f.html
# https://wenku.baidu.com/view/d15646ce5fbfc77da269b1c7.html
import re
import time
import os
from urllib import parse
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


# 加载文档内容
def is_docm_load(brower):
    submit = brower.find_element_by_class_name('foldpagewg-text')
    # submit = wait.until(EC.presence_of_element_located((By.XPATH, 'div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div/div[1]')))
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", submit)  # 让当前元素不可见区域在浏览器可见
    submit.click()

    while  True:
        time.sleep(3)
        more = brower.find_element_by_class_name('pagerwg-schedule')
        print('正在加载：',more.text)  #pagerwg-schedule
        load_com = re.search('(\d{0,2})\%', more.text)
        if not load_com:
            break
        submit = brower.find_element_by_class_name('pagerwg-button')
        # submit = wait.until(EC.presence_of_element_located(By.XPATH, 'div[2]/div[2]/div[6]/div[3]/div[1]/div[1]'))
        brower.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", submit)   #让当前元素不可见区域在浏览器可见
        submit.click()

# 判断当目录是否包含 contents 目录，创建并返回该目录路径
def is_filedic_ex(contents):

    wenkuml = os.path.join(os.getcwd(),contents)
    if not os.path.isdir(wenkuml):
        os.mkdir(wenkuml)
        print('创建目录：',contents)
    return contents

# 将brower page
def file_write(brower, contents):
    filename = os.path.basename(parse.urlparse(brower.current_url).path)
    filepath = '%s\%s' % (contents, filename)
    with open(filepath,'w',encoding='utf-8') as f:
        f.write(brower.page_source)
    print('网页源码已经保存：',filepath)


if __name__ == '__main__':

    # wkurl = 'https://wenku.baidu.com/view/c7d1617b27284b73f24250fb.html'
    wkurl = input('请输入百度文库网址：')

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    # options.add_argument('User-Agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0"')
    options.add_argument(('--headless'))
    driver = webdriver.Chrome(options=options)

    # 打开文库
    driver.get(wkurl)
    print('正在打开网页：',wkurl)

    # //div[2]/div[2]/div[6]/div[3]/div[1]/div[1]   点击加载更多
    # //div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/div/div[1] 继续阅读
    # 判断 继续阅读foldpagewg-text  点击加载更多 (pagerwg-button)是否存在    剩余0%未读 pagerwg-schedule

    # is_docm_load(driver)    # class foldpagewg-text

    # 判断当目录是否包含 wenku 目录，创建并返回该目录路径
    wenkuml = is_filedic_ex('wenku')

    # 将解析后的网页写入文件  以URL命名
    file_write(driver,wenkuml)

    # 解析文章标题和页码
    title = driver.find_element_by_class_name('doc-title').text
    page = driver.find_element_by_class_name('pages-number').text
    print('文章标题：%s' % title)
    print('文章页数：%s' % page)

    # 解析正文

    itemall2 = driver.find_elements_by_xpath('//*/div/div/div/div/div/p')
    x = 0
    filepath = os.path.join(is_filedic_ex('wenku'), title + '.txt')
    with open(filepath, 'w', encoding='utf-8') as f:
        for x in range(0,len(itemall2)):
            f.write(itemall2[x].text+'\n')
            print('第%s次提取：'%x,itemall2[x].text)
    f.close()
    print('文档内容已经保存：',filepath)

    # 关闭浏览器
    driver.quit()