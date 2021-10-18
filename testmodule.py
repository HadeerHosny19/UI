@author
from selenium import webdriver
import time
import unittest
from exceldatareader import DataReader

class MyTest01x(unittest.TestCase):
    def setup(self):
        self.driver=webdriver.chrom()
    def test_login(self):
        driver= self.driver
        try:
            driver.get('https://www.facebook.com/login/')
            driver.maximize_window()
        except exception as ex:
            print(ex)
        else:
            time.sleep(10)
            driver.find_element_by_id('loginbutton').click()
            time.sleep(5)
            cur_url = driver.current_url
            expected_url = 'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjM0NTYyNzQ1LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D'
            try:
                self.assertEqual(cur_url, expected_url, 'Failed!')
            except exception as ex:
                print(ex)

            phone_number = driver.find_element_by_id("email")
            password = driver.find_element_by_id('pass')
            time.sleep(5)
            uname,pwd = DataReader.readDataForLogin()
            phone_number.clear()
            password.clear()
            phone_number.send_keys(pwd)
            time.sleep(5)
            driver.find_element_by_id('loginbutton').click()
            time.sleep(10)
            cur_url = driver.current_url
            expected_url = 'https://www.facebook.com/myaccount/'
            try:
                self.assertEqual(cur_url, expected_url, "Not able to login")
            except exception as ex:
                print("Username and password is in correct {}".format(ex))
            time.sleep(20)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()