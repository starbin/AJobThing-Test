#import needed library
import unittest
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestSoulusi(unittest.TestCase):
    #setup capabilities
    def setUp(self):
        desired_caps = {}
        #set capabilities for unicode keyboard
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        #setting android and emulator
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Nexus5X'
        #setting appname
        desired_caps['app'] = PATH('./Soulusi 1.0.12-develop-release.apk')

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    #first test case
    def test_like_without_login(self):
        #wait until next button to appear after splash screen
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Next']")))
        #find element next button and click it
        el = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el.click()
        self.driver.implicitly_wait(10)
        el2 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el2.click()
        self.driver.implicitly_wait(10)
        el3 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el3.click()
        #wait until like button is clickable
        EC.element_to_be_clickable((By.XPATH, "//android.widget.LinearLayout"))
        #find element like button by coordinates and click it
        thmb = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@bounds='[42,1011][210,1074]']")
        thmb.click()
        #wait for facebook button and assert it
        fb_btn = EC.element_to_be_clickable((By.XPATH, "//[@id='my.soulusi.androidapp.develop:id/btn_facebook']"))
        self.assertIsNotNone(fb_btn)

    #second test case
    def test_next_back(self):
        # wait until next button to appear after splash screen
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Next']")))
        # find next button and clicked it, 2 times
        el = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el.click()
        self.driver.implicitly_wait(10)
        el2 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el2.click()
        #find back button and click it, 2 times
        el4 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Back']")
        el4.click()
        self.driver.implicitly_wait(10)
        el5 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Back']")
        el5.click()
        self.driver.implicitly_wait(10)
        # find next button and clicked it, 3 times
        el7 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el7.click()
        self.driver.implicitly_wait(10)
        el8 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el8.click()
        self.driver.implicitly_wait(10)
        el9 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el9.click()
        self.driver.implicitly_wait(10)
        #asserting that main menu is displayed by toolbar button
        EC.element_to_be_clickable((By.XPATH, "//[@id='my.soulusi.androidapp.develop:id/btn_toolbar_menu']"))


    def test_login_using_random_email_and_password(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Next']")))
        el = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el.click()
        self.driver.implicitly_wait(10)
        el2 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el2.click()
        self.driver.implicitly_wait(10)
        el3 = self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']")
        el3.click()
        EC.element_to_be_clickable((By.XPATH, "//android.widget.LinearLayout"))
        thmb = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@bounds='[42,1011][210,1074]']")
        thmb.click()
        fb_btn = EC.element_to_be_clickable((By.XPATH, "//[@id='my.soulusi.androidapp.develop:id/btn_facebook']"))
        #find and click login button
        login_btn = self.driver.find_element_by_id("my.soulusi.androidapp.develop:id/btn_login")
        login_btn.click()
        #wait until email form is located
        EC.presence_of_element_located((By.ID, "my.soulusi.androidapp.develop:id/et_email"))
        email = self.driver.find_element_by_id("my.soulusi.androidapp.develop:id/et_email")
        #type email as email
        email.send_keys("email")
        #find password form and write password as password
        passwd = self.driver.find_element_by_id("my.soulusi.androidapp.develop:id/et_password")
        passwd.send_keys("password")
        #click login button
        btn_login = self.driver.find_element_by_id("my.soulusi.androidapp.develop:id/btn_login")
        btn_login.click()
        #asserting by warning id is displayed
        self.assertTrue(self.driver.find_element_by_id("my.soulusi.androidapp.develop:id/tvText").is_displayed())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSoulusi)
    unittest.TextTestRunner(verbosity=2).run(suite)