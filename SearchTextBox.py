import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class SearchTextBox(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        inst.driver = webdriver.Chrome(PATH)
        inst.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get('http://automationpractice.com')

    def test_search_text(self):

        # search text in textbox
        self.search_field = self.driver.find_element_by_id('search_query_top')
        self.search_field.send_keys('dress')
        self.search_field.submit()

        # select view list grid
        self.search_field = self.driver.find_element_by_id('grid')
        self.search_field.click()
        time.sleep(2)
        self.search_field = self.driver.find_element_by_id('list')
        self.search_field.click()

        # sort by
        self.search_field = self.driver.find_element_by_id('selectProductSort')
        self.search_field.click()
        self.driver.find_element_by_xpath("//select[@id='selectProductSort']/option[text()='Price: Lowest first']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//select[@id='selectProductSort']/option[text()='Price: Highest first']").click()
        # self.search_field.select_by_value('price:desc')
        # self.driver.implicitly_wait(3)

    # @classmethod
    # def tearDownClass(inst):
    #     # close the browser window
    #     inst.driver.quit()

if __name__ == '__main__':
    unittest.main()