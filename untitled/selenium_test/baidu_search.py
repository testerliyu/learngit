from selenium import webdriver
import os
import time
import io
import csv
s = 'baidu\r12345\rselenium'
with open('E://info.txt','w') as f:
       f.write(s)
       f.close()

file_info = open('E://info.txt','r')
values = file_info.readlines()
file_info.close()

#my_file = 'info.csv'
#date = csv.reader(file(my_file,'rb'))
#for user in date:
 #   print(user)

for search in values:
    driver =  webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    driver.quit()
    print(search)