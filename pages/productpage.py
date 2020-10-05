from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
class ProductPage():
    def __init__(self, driver):
        self.driver = driver

        #define locator here
        self.addcart_button_xpath = "//*[contains(text(),'Add to Cart')]"

        self.login_popup_xpath = "//*[contains(text(),'Welcome! Please Login to continue.')]"
        self.username_textbox_xpath = "//[@placeholder='Please enter your Phone Number or Email']"
        self.password_textbox_xpath = "//[@placeholder='Please enter your password']"
        self.login_button_xpath = "//*[contains(@text(),'LOGIN')]"

    def wait_resultpage_load(self):
        Wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.addcart_button_xpath)))

    def click_add_to_cart(self):
        self.driver.find_element_by_xpath(self.addcart_button_xpath).click()

    def wait_login_popup_loaded(self):
        Wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.password_textbox_xpath)))

    def input_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def input_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def user_click_add_to_cart(self):
        self.wait_resultpage_load()
        self.click_add_to_cart()

    def user_login(self, username, password):
        self.wait_login_popup_loaded()
        self.input_username(username)
        self.input_password(password)
        self.click_login()



