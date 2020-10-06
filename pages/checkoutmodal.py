from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutModal():
    def __init__(self, driver):
        self.driver = driver

        #define locator here
        self.checkout_button_xpath = "//button[contains(text(),'CHECK OUT')]"

    def wait_checkout_modal_load(self):
        Wait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button_xpath)))

    def click_add_to_cart(self):
        checkout_button = self.driver.find_element_by_xpath(self.checkout_button_xpath)
        self.driver.execute_script("arguments[0].click();", checkout_button)

    def user_click_checkout_button(self):
        self.wait_checkout_modal_load()
        self.click_add_to_cart()
