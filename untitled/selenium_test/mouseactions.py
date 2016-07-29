from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
#driver.set_window_size(480,800)#设置浏览器的宽480，高800
#driver.close()
# size = driver.find_element_by_id('kw').size
# print(size)#获得输入框的尺寸
#
# text = driver.find_element_by_id('cp').text
# print(text)#返回百度页面底部备案信息
#
# attribute = driver.find_element_by_id('kw').get_attribute('type')
# print(attribute)#返回元素的属性值
#
# result = driver.find_element_by_id('kw').is_displayed()
# print(result)#返回元素的结果是否可见，返回结果为true或false
# above = driver.find_element_by_link_text('***')
# ActionChains(driver).move_to_element(above).perform()#对定位到的元素执行鼠标悬停操作
# ActionChains(driver).double_click(above).perform()鼠标左键双击
# ActionChains(driver).context_click().perform()鼠标右击
# element = driver.find_element_by_class_name('****')定位元素的原位置
# target = driver.find_element_by_class_name('****')定位元素要移动到的目标位置
# ActionChains(driver).drag_and_drop(element,target).perform()执行元素的拖放操作
time.sleep(5)
driver.quit()
