from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'D:\python\Python-3.7.4\Lib\site-packages\chromedriver.exe')
type(browser)

browser.get('http://10.1.2.36/login/Login.jsp?logintype=1')
# linkElem = browser.find_element_by_link_text('登录')
# linkElem.click() 
# print(browser.page_source)
loginElem = browser.find_element_by_id('loginid')
print(str(loginElem))
loginElem.send_keys('61309011')
passwordElem = browser.find_element_by_id('userpassword')
print(str(passwordElem))
passwordElem.send_keys('wl123456')

passwordElem.submit()
alerta=browser.find_element_by_id('_DialogTable_1566360277381')
alerta.send_keys(Keys.RETURN)
# webdriver.common.alert.Alert(browser).accept()
# alert.Alert(browser).accept()
# browser.close()