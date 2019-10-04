from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'D:\python\Python-3.7.4\Lib\site-packages\chromedriver.exe')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
print(elem)
elem.clear()
elem.send_keys("lists")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()