from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
class ProductPage():
    def __init__(self, driver):
        self.driver = driver

        #define locator here
        self.addcart_button_xpath = "//*[contains(text(),'Add to Cart')]"

        self.username_textbox_xpath = "//input[@placeholder='Please enter your Phone Number or Email']"
        self.password_textbox_xpath = "//input[@placeholder='Please enter your password']"
        self.login_button_xpath = "//*[contains(text(),'LOGIN')]"

    def wait_resultpage_load(self):
        Wait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.addcart_button_xpath)))

    def click_add_to_cart(self):
        add_to_cart_button = self.driver.find_element_by_xpath(self.addcart_button_xpath)
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)

    def wait_login_popup_loaded(self):
        Wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button_xpath)))

    def input_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def input_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element_by_xpath(self.login_button_xpath)
        self.driver.execute_script("arguments[0].click();", login_button)

    def user_click_add_to_cart(self):
        self.wait_resultpage_load()
        self.click_add_to_cart()

    def user_login(self, username, password):
        self.wait_login_popup_loaded()

        login_frame_modal = self.driver.find_element_by_class_name("login-iframe")
        self.driver.switch_to.frame(login_frame_modal)  # switch to frame

        self.input_username(username)
        self.input_password(password)
        self.click_login()

        self.driver.switch_to.default_content()  #switch back to default frame





