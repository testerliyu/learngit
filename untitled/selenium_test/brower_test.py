from selenium import webdriver
import  time
import os
import  io
from io import FileIO
from PIL import Image
browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
time.sleep(5)

#浏览器最大化
browser.maximize_window()
browser.find_element_by_id('kw').send_keys('python+selenium')
browser.find_element_by_id('su').click()
time.sleep(5)
browser.find_element_by_id('kw').clear()
time.sleep(5)
browser.get_screenshot_as_file('C:\\baidu.jpg')#截屏保存为baidu.jpg
for x in  browser.get_cookies():
  #  with open('C:\\cookies.txt','w')as f:
   #     f.write(x)
     print('the %d cookies : \r %r'% (len(x),x))
try:
     browser.find_element_by_id('kw_2').send_keys('Python自动化实例')#元素不对，产生异常
     browser.find_element_by_id('su').click()
     time.sleep(5)
except:
     browser.save_screenshot('C:\\baidu2.jpg')#截屏保存为baidu2.jpg
     print('截屏成功')
browser.refresh()#刷新
browser.back()#后退
time.sleep(5)
browser.forward()#前进
time.sleep(5)
browser.quit()