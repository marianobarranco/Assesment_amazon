from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class ProductPage():

    def __init__(self, driver):
        self.driver = driver

        '''Locator Variables'''

        self.product_title_id = "productTitle"
        self.product_price_class = "a-price"
        self.quantity_dropdown_id = "quantity"
        self.dropdown_option_three_xpath = "//*[@id='quantity']/option[3]"
        self.add_to_cart_id = "add-to-cart-button"
        self.go_to_basket_button_xpath = "//a[contains(text(),'Go to basket')]"

        '''Methods'''

    def store_product_information(self):

        '''Store product name'''

        product_title = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.product_title_id))).text



        '''Store product price'''
        product_price_title = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.product_price_class))).text

        product_price = product_price_title[3:]


        '''Store price for three items'''

        product_prince_int = float(product_price)
        product_price_x3 = str(product_prince_int*3)

        data = {"product_title":product_title, "product_price_x3":product_price_x3, "product_price":product_price}

        with open("Amazon/resources/miscfiles/product_info.json","w")as outfile:
            json.dump(data,outfile)


    def add_three_items_to_cart(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.quantity_dropdown_id))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                self.dropdown_option_three_xpath))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.add_to_cart_id))).click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.go_to_basket_button_xpath))).click()

