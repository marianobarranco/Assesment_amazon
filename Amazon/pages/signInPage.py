from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage():

    def __init__(self,driver):
        self.driver = driver

        '''Non Locator Variables'''
        self.signin_url = "https://www.amazon.ae/ap/signin"
        self.lists_url = "https://www.amazon.ae/hz/wishlist/intro"

        '''Locator Variables'''
        self.email_field_id = "ap_email"
        self.submit_button_id = "continue"
        self.alert_message_class = "a-alert-heading"
        self.signin_title_xpath = "//h1[contains(text(),'Sign in')]"

        '''Methods'''
    def go_to_amazon_ae_page(self):
        self.driver.get("https://www.amazon.ae")

    def enter_valid_email(self):
        import random
        number = random.randint(0000,9999)
        str_number = str(number)

        email = "myfakemail"+str_number+"@marianob.bar"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.email_field_id))).send_keys(email)

    def click_submit(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.submit_button_id))).click()

    def verify_current_url(self):
        current_url = self.driver.current_url
        assert current_url == self.signin_url

    def verify_alert_message(self):
        title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,
                              self.alert_message_class))).is_displayed()
        assert title == True

    def validate_page(self,page):
        if page == "lists":
            current_url = self.driver.current_url

            assert current_url == self.lists_url

        else:
            sign_in_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 self.signin_title_xpath))).is_displayed()
            assert sign_in_title == True

