import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

class HomePage(unittest.TestCase):
    def setUp(self):
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com')
    
    #redirect contact us
    # def test_redirect_contact_us(self):
    #     self.search_field = self.driver.find_elements_by_id('contact-link')
    #     self.search_field.click()
    #     self.driver.title == 'Contact us - My Store'

    #redirect sign in
    # def test_redirect_sign_in(self):
    #     self.search_field = self.driver.find_element_by_xpath("//a[@class='login']")
    #     self.search_field.click()
    #     self.driver.title == 'Login - My Store'

    #redirect shopping cart
    # def test_redirect_shopping_cart(self):
    #     self.search_field = self.driver.find_element_by_xpath("//div[@class='shopping_cart']/a")
    #     self.search_field.click()
    #     self.driver.title == 'Order - My Store'
    
    #search text box without waiting suggestion
    # def test_text_box(self):
    #     self.search_field = self.driver.find_element_by_id('search_query_top')
    #     self.search_field.send_keys('dress')
    #     self.search_field.submit()
    #     self.driver.title == 'Search - My Store'

    
    #search text box witho waiting suggestion
    # def test_suggest_text_box(self):
    #     self.search_field = self.driver.find_element_by_id('search_query_top')
    #     self.search_field.send_keys('dress')

    #     try:
    #         self.search_field = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "//div[@class='ac_results']"))
    #         )
    #         self.search_field.click()
    #         if 'dress' in self.driver.title:
    #             pass

    #     except:
    #         self.driver.quit()
        

    # hover women dress tshirt
    # def test_hover_tab(self):

        # hovering for single element
        # element_to_hover_over = self.driver.find_element_by_xpath("//li/a[@class='sf-with-ul']")
        # hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        # hover.perform()
        # try:
        #     self.search_field = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//ul/li[@class='sfHover']"))
        #     )

        # except:
        #     self.driver.quit()

        # hovering for multiple element
        # elements_to_hover_over = self.driver.find_elements_by_xpath("//li/a[@class='sf-with-ul']")
        # for element in elements_to_hover_over:
        #     ActionChains(self.driver).move_to_element(element).perform()
        #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul/li[@class='sfHover']")))
            
    # def test_tab_popular_best(self):
        # first we have to scroll to the element so we can clearly see what happend when script get execute
        # view = self.driver.find_element_by_id('center_column')
        # self.driver.execute_script("arguments[0].scrollIntoView();", view)

        # elements = self.driver.find_elements_by_xpath("//ul[@id='home-page-tabs']/li/a")
        # for i in elements:
        #     i.click()
    
    def test_quickview(self):
        view = self.driver.find_element_by_id('center_column')
        self.driver.execute_script("arguments[0].scrollIntoView();", view)
        self.searh_field = self.driver.find_element_by_xpath("//div[@class='product-image-container']/a")
        self.searh_field.click()
        try:
            self.search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "product"))
            )

        except:
            self.driver.quit()
        
    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()