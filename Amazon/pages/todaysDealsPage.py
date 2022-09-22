from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TodaysDeals():

    def __init__(self,driver):
        self.driver = driver


        '''Locator Variables'''

        self.second_category_xpath = "//*[@id='grid-main-container']/div[3]/div/div[2]/div/div/a[1]/div/div/img"
        self.first_item_xpath = "//*[@id='octopus-dlp-asin-stream']/ul/li[1]/span/div/div[1]/a/div"
        '''Methods'''

    def select_second_category(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.second_category_xpath))).click()

    def select_first_item(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.first_item_xpath))).click()
        except:
            pass

