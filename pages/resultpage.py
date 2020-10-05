from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
class ResultPage():
    def __init__(self, driver):
        self.driver = driver

        #define locator here
        self.product_grouping_card = "//div[@data-qa-locator='product-item']"

    def wait_resultpage_load(self):
        Wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_grouping_card)))

    def select_first_product(self):
        self.driver.find_element_by_xpath(self.product_grouping_card).click()

    def user_select_first_product(self):
        self.wait_resultpage_load()
        self.select_first_product()
