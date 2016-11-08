from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest,time

class Baidu(unittest.TestCase):
    '''百度测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.baidu.com'

    def test_baidu_search(self):
        '''百度搜索关键字htmltestcase'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('htmltestrunner')
        driver.find_element_by_id('su').click()
        title = driver.title
        time.sleep(3)
        self.assertEqual(title,'htmltestrunner_百度搜索')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu_search'))
    dateTimeStmap = time.strftime('%Y%m%d_%H_%M_%S')
    #filename = 'E://result.html'
    fp = open('E://report'+'_'+dateTimeStmap+'.html','wb')
    #with open(filename,'wb')as fp:
    runner = HTMLTestRunner(stream =fp,title = '测试报告',description = '用例执行情况')
    runner.run(testunit)
    fp.close()
