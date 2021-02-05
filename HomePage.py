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
    def test_redirect_contact_us(self):
        self.search_field = self.driver.find_elements_by_id('contact-link')
        self.search_field.click()
        self.driver.title == 'Contact us - My Store'

    #redirect sign in
    def test_redirect_sign_in(self):
        self.search_field = self.driver.find_element_by_xpath("//a[@class='login']")
        self.search_field.click()
        self.driver.title == 'Login - My Store'

    #redirect shopping cart
    def test_redirect_shopping_cart(self):
        self.search_field = self.driver.find_element_by_xpath("//div[@class='shopping_cart']/a")
        self.search_field.click()
        self.driver.title == 'Order - My Store'
    
    #search text box without waiting suggestion
    def test_text_box(self):
        self.search_field = self.driver.find_element_by_id('search_query_top')
        self.search_field.send_keys('dress')
        self.search_field.submit()
        self.driver.title == 'Search - My Store'

    
    #search text box with waiting suggestion
    def test_suggest_text_box(self):
        self.search_field = self.driver.find_element_by_id('search_query_top')
        self.search_field.send_keys('dress')

        try:
            self.search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='ac_results']"))
            )
            self.search_field.click()
            if 'dress' in self.driver.title:
                pass

        except:
            self.driver.quit()
        

    # # hover women dress tshirt
    def test_hover_tab(self):

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
        elements_to_hover_over = self.driver.find_elements_by_xpath("//li/a[@class='sf-with-ul']")
        for element in elements_to_hover_over:
            ActionChains(self.driver).move_to_element(element).perform()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul/li[@class='sfHover']")))
            
    def test_tab_popular_best(self):
        # first we have to scroll to the element so we can clearly see what happend when script get execute
        view = self.driver.find_element_by_id('center_column')
        self.driver.execute_script("arguments[0].scrollIntoView();", view)

        elements = self.driver.find_elements_by_xpath("//ul[@id='home-page-tabs']/li/a")
        for i in elements:
            i.click()

    def test_hover_items_popbest(self):
        view = self.driver.find_element_by_id('center_column')
        self.driver.execute_script("arguments[0].scrollIntoView();", view)
        elements_to_hover_over = self.driver.find_elements_by_xpath("//ul[@id='homefeatured']/li/div[@class='product-container']")
        for element in elements_to_hover_over:
            ActionChains(self.driver).move_to_element(element).perform()
            # wait until classname hovered appear
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hovered")))
    
    def test_quickview(self):
        view = self.driver.find_element_by_id('center_column')
        self.driver.execute_script("arguments[0].scrollIntoView();", view)
        self.searh_field = self.driver.find_element_by_xpath("//div[@class='product-image-container']/a")
        self.searh_field.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "product"))
            )

        except:
            self.driver.quit()

    def test_btn_more(self):
        view = self.driver.find_element_by_id('center_column')
        self.driver.execute_script("arguments[0].scrollIntoView();", view)

        # get title from attribute title on tag <a title='a title here' />
        a_title = self.driver.find_element_by_xpath("//div[@class='product-image-container']/a[@class='product_img_link']").get_attribute('title')

        element = self.driver.find_element_by_xpath("//ul[@id='homefeatured']/li/div[@class='product-container']")
        ActionChains(self.driver).move_to_element(element).perform()

        self.search_field = self.driver.find_element_by_class_name("lnk_view")
        self.search_field.click()

        # check if the title page same as product we clicked
        self.driver.title == f'{ a_title } - My Store'

    def test_add_cart(self):
        view = self.driver.find_element_by_id('center_column')
        self.driver.execute_script("arguments[0].scrollIntoView();", view)

        element = self.driver.find_element_by_xpath("//ul[@id='homefeatured']/li/div[@class='product-container']")
        ActionChains(self.driver).move_to_element(element).perform()

        self.search_field = self.driver.find_element_by_class_name("ajax_add_to_cart_button")
        self.search_field.click()

        # wait until css of element with id 'layer_cart' change display: block
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='layer_cart'][contains(@style, 'display: block')]"))
            )

        except:
            self.driver.quit()

        self.continue_shopping = self.driver.find_element_by_class_name("continue")
        self.continue_shopping.click()

        element_cart = self.driver.find_element_by_xpath("//div[@class='shopping_cart']/a")
        ActionChains(self.driver).move_to_element(element_cart).perform()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='cart_block block exclusive'][contains(@style, 'display: block')]"))
            )

        except:
            self.driver.quit()

        quantity = self.driver.find_element_by_xpath("//span[@class='quantity-formated']/span").text
        a_title = self.driver.find_element_by_class_name("cart_block_product_name").get_attribute("title")
        
        # check if the cart contain item we already chosed
        # the item is Faded Short Sleeve T-shirts and quantity is 1
        if quantity == 1 and a_title == 'Faded Short Sleeve T-shirts':
            True
        
    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()