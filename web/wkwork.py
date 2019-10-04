# -*- coding:utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

url = input("输入文档链接，搞快点：")
driver.get(url)

error_str = ""

try:
    page_num = driver.find_element_by_xpath("//span[@class='page-count']").text

    find_button = driver.find_element_by_xpath("//div[@class='doc-banner-text']")
    driver.execute_script("arguments[0].scrollIntoView();", find_button)
    button = driver.find_element_by_xpath("//span[@class='moreBtn goBtn']")
    button.click()

    for i in range(1, int(page_num.strip('/')) + 1):
        page = driver.find_element_by_xpath("//div[@data-page-no='{}']".format(i))
        driver.execute_script("arguments[0].scrollIntoView();", page)
        time.sleep(0.3)
        print(driver.find_elements_by_xpath("//div[@data-page-no='{}']//div[@class='reader-txt-layer']".format(i))[-1].text)

except NoSuchElementException:
    if driver.find_element_by_xpath("//div[@class='doc-bottom-text']").text == "试读已结束，如需继续阅读或下载":
        error_str = "\n------------------------------------------------------------------\n\n" \
                    "----------百度文库提示试读已结束啦，无法爬取全文，等会再试试吧----------\n\n" \
                    "------------------------------------------------------------------"

finally:
    print(error_str)