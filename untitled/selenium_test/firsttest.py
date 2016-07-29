from selenium import webdriver
import time
import re
import pdb
browser = webdriver.Firefox()

browser.get('http://www.baidu.com')
pdb.set_trace()     #设置断点   输入n单步执行
print(browser.title)
time.sleep(3)
browser.find_element_by_id('kw').send_keys('糗事百科')
browser.find_element_by_id('su').click()
time.sleep(3)
browser.find_element_by_class_name('favurl').click()
time.sleep(3)
browser.quit()
