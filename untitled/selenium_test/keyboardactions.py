from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC#导入模块作为EC
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
title = browser.title
print(title)
url =  browser.current_url
print(url)
browser.find_element_by_link_text('登录').click()
browser.implicitly_wait(10)    #隐式等待
element = browser.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__userName']")
#element = WebDriverWait(browser,5,0.5).until(
#   EC.presence_of_element_located(By.XPATH,"//*[@id='TANGRAM__PSP_8__userName']")#显示等待五分钟，超时抛出异常
#)
element.clear()
element.send_keys('唯一surpermen')
time.sleep(5)
browser.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__password']").send_keys('li11056..')
browser.find_element_by_id('TANGRAM__PSP_8__submit').click()
now_title = browser.title
print(now_title)
now_url = browser.current_url
print(now_url)
text = browser.find_element_by_xpath("//*[@id='s_username_top']").text
print(text)
browser.quit()