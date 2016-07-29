from selenium import  webdriver
import  time
import logging
#操作js操作滚动条
logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(5)
#拖动滚动条到底部
js = 'var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)
time.sleep(5)

#拖动滚动条都顶部
js_ = 'var q=document.documentElement.scrollTop=0'
driver.execute_script(js_)
time.sleep(5)

driver.quit()

