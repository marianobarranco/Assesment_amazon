from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json

class BasketPage():

    def __init__(self, driver):

        self.driver = driver

        '''Locator Variables'''
        self.product_title_basket_xpath="/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/ul/li[1]/span"
        self.item_count_id = "sc-subtotal-label-activecart"
        self.item_price_class = "sc-product-price"
        self.subtotal_title_id = "sc-subtotal-amount-activecart"

        '''Methods'''

    def switch_to_iframe(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,
                                                                               "checkoutPrefetch;")))

    def validate_product_title_and_quantity(self):
        with open("Amazon/resources/miscfiles/product_info.json") as f:
            data = json.loads(f.read())
            full_title = (data["product_title"])

        short_title = full_title[:30]
        '''Store product name in basket -- USE FULL XPATH'''
        title_basket = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                            self.product_title_basket_xpath))).text


        '''Store item quantity'''
        item_count = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,
                                                                                    self.item_count_id))).text

        quantity = str(item_count[10:11])

        '''Assertions'''
        assert short_title in title_basket
        assert quantity == "3"


    def validate_price_and_subtotal(self):
        with open("Amazon/resources/miscfiles/product_info.json") as f:
            data = json.loads(f.read())
            product_price = (data["product_price"])
            subtotal = (data["product_price_x3"])

        '''Store item price'''
        title_price = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                            self.item_price_class))).text
        basket_price = str(title_price[4:])

        '''Store subtotal'''
        title_subtotal = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,
                                                                                             self.subtotal_title_id))).text
        basket_subtotal = str(title_subtotal[5:])


        '''Assertions'''
        assert basket_subtotal == subtotal
        assert basket_price == product_price