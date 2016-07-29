from selenium import webdriver



driver = webdriver.Firefox()
driver.get('http://207.46.141.169:8081/login')
driver.implicitly_wait(10)
driver.find_element_by_id('buttonId').click()
currentt_url = driver.current_url
assert currentt_url=='207.46.141.169:8081/apps'    'the url is wrong'
print('the url is right')
driver.close()