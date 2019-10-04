
from selenium import webdriver
import  time


if __name__ == '__main__':
    url = r'http://oa.cqszfy.com:10000'
    url = r'http://172.1.2.36/'
    wb_oa = webdriver.Chrome()
    wb_oa.get(url)

    # 模拟登录
    wb_oa.find_element_by_id('loginid').send_keys('61309011')
    wb_oa.find_element_by_id('userpassword').send_keys('wl123456')
    wb_oa.find_element_by_id('login').submit()
    print(wb_oa.current_url)
    time.sleep(10)
    # 定位元素
    leftid = wb_oa.find_element_by_id("leftMenu")  # 左边连接

    print(leftid.text)
    wb_oa.find_element_by_id("portal2").click()  # 医院主页
    print(wb_oa.current_url)
    time.sleep(2)
    # wb_oa.find_element_by_id("portal21").click()    # 个人主页
    print(wb_oa.current_url)
    top = wb_oa.find_element_by_class_name("topMenuDiv_top")    # 上面连接
    print(top.text)
    wb_oa.switch_to.frame("mainFrame") # 切换标签
    oafile = wb_oa.find_elements_by_xpath(r'//*[@id="_contenttable_101"]/tbody/tr/td/table/tbody/tr/td/a') #通过XPATH查找信息
    for i in range(0,len(oafile)):
        print(oafile[i].text,oafile[i].get_attribute('href'))  # 获取属性值





