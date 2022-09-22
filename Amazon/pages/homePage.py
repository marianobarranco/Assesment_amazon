from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage():

    def __init__(self,driver):
        self.driver = driver


        '''Locator Variables'''
        self.hm_menu_class = "hm-icon"
        self.avatar_icon_id = "hmenu-customer-avatar-icon"
        self.todays_deals_xpath = "//a[contains(text(),'Today')]"
        self.account_lists_id = "nav-link-accountList"
        self.adresses_xpath = "//span[contains(text(),'Your Addresses')]"
        self.orders_xpath = "//span[contains(text(),'Your Orders')]"
        self.lists_xpath = "//span[contains(text(),'Your Lists')]"


        '''Methods'''
    def go_to_amazon_ae_page(self):
        self.driver.get("https://www.amazon.ae")

    def click_hamburger_navigation_menu(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, self.hm_menu_class))).click()

    def click_avatar_icon(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.avatar_icon_id))).click()

    def click_todays_deals(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.todays_deals_xpath))).click()

    def hover_over_account_menu(self):
        a = ActionChains(self.driver)
        m = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.account_lists_id)))
        a.move_to_element(m).perform()


    def select_option(self,option):
        if option == "addresses":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.adresses_xpath))).click()

        elif option == "orders":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.orders_xpath))).click()

        else:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.lists_xpath))).click()



