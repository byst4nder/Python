#! python3
# 硒主要用于编写测试用例。该硒 包本身不提供测试工具/框架。您可以使用Python的unittest模块编写测试用例。工具/框架的其他选项是py.test和nose。

# 在本章中，我们使用unittest作为选择框架。以下是使用unittest模块的修改示例。这是对python.org搜索功能的测试：

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\python\Python-3.7.4\Lib\site-packages\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()