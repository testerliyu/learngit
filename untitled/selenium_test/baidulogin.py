from selenium.webdriver.common.action_chains import ActionChains
def login(driver):
    driver.find_element_by_link_text('登录').click()
    driver.implicitly_wait(10)
    driver.find_element_by_id('TANGRAM__PSP_8__userName').clear()
    driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('唯一surpermen')
    driver.find_element_by_id('TANGRAM__PSP_8__password').clear()
    driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('li11056..')
    driver.find_element_by_id('TANGRAM__PSP_8__submit').click()

def logout(driver):
    above = driver.find_element_by_class_name('user-name')
    ActionChains(driver).move_to_element(above).perform()  # 对定位到的元素执行鼠标悬停操作
    driver.find_element_by_class_name('quit').click()
    driver.find_element_by_xpath("//*[@id='tip_con_wrap']/div[3]/a[3]").click()