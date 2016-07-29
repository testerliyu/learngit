from selenium import webdriver
from selenium_test import baidulogin
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
baidulogin.login(driver)
title = driver.find_element_by_class_name('user-name').text
if title == '唯一surpermen':
    print('登录成功')
else:
    print('登录失败')
baidulogin.logout(driver)
print('退出成功')
driver.quit()