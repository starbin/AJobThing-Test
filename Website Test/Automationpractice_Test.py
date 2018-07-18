
#import library needed
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class PythonOrgSearch(unittest.TestCase):

    #make setup def
    def setUp(self):
        #declare to use Firefox
        self.driver = webdriver.Firefox()
        #make variable for easy access
        driver = self.driver
        #maximize Firefox
        driver.maximize_window()

    #first Test Case, accessing site
    def test_access_site(self):
        driver = self.driver
        #go to Web Under Test
        driver.get("http://automationpractice.com/")
        #asserting that there is shopping cart in page source, so we know that we already in index
        assert "shopping_cart" in driver.page_source

    #second Test Case, Searching some items
    def test_search(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        #asserting My Store in browser title, so we know that we already in index
        self.assertIn("My Store", driver.title)

        #find element using ID search_query_top, and set variable
        elem = driver.find_element_by_id("search_query_top")
        #type some text to search
        elem.send_keys("dress")
        #simulate Enter key in keyboard
        elem.send_keys(Keys.RETURN)
        #wait until there is text results have been found. in page, so we know search is done
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'results have been found.')]")))
        #make sure that one of the item we search is in page source
        assert "Printed Summer Dress" in driver.page_source

    #Third Test Case, adding cart from index page
    def add_cart_from_index(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("My Store", driver.title)

        #set webdriverwait in variable for easy access
        wait = WebDriverWait(driver, 10)
        #set actionchains in variable for easy access
        actions = ActionChains(driver)

        #find element text by id
        hover_element = driver.find_element_by_link_text('Faded Short Sleeve T-shirts')
        #scroll browser to element
        driver.execute_script("return arguments[0].scrollIntoView();", hover_element)

        #simulate hover to element using actionchains
        actions.move_to_element(hover_element).perform()
        #locate and click add to cart button
        submenu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ajax_add_to_cart_button")))
        submenu.click()
        #locate and click continue button
        addcart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".continue")))
        addcart.click()
        #assert to make sure test is success
        assert "$18.51" in driver.page_source

    def test_wrong_format_email(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("My Store", driver.title)

        #set varibal as empty array because of this is elements
        find_login_btn = []
        find_login_btn = driver.find_elements_by_class_name('login')
        #click the first login button in array and go to login page
        find_login_btn[0].click()

        #wait until id email_create is located
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'email_create')))
        #find register email form
        find_email_reg = driver.find_element_by_id('email_create')
        #input wrong format email and press enter
        find_email_reg.send_keys("ini-email")
        find_email_reg.send_keys(Keys.RETURN)
        #wait until Invalid email address present and assert it
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid email address.')]")))
        assert "Invalid email address." in driver.page_source

    def test_false_login(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("My Store", driver.title)

        find_login_btn = []
        find_login_btn = driver.find_elements_by_class_name('login')
        find_login_btn[0].click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email_create')))

        #find email form and add unregistered email
        find_email = driver.find_element_by_id('email')
        find_email.send_keys("ini-email@gmail.com")
        #find password form and add random password
        find_pass = driver.find_element_by_id('passwd')
        find_pass.send_keys("ini-password")
        #find submit button and click it
        submit_btn = driver.find_element_by_id('SubmitLogin')
        submit_btn.click()

        #wait until there is authentication failed warning and assert it
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Authentication failed.')]")))
        assert "Authentication failed." in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
