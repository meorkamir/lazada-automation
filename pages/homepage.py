from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
class HomePage():
    def __init__(self, driver):
        self.driver = driver

        #define locator here
        self.search_textbox_id = "q"
        self.search_button_class = "search-box__button--1oH7"

    def wait_homepage_load(self):
        Wait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.search_textbox_id)))

    def search_item(self, item):
        self.driver.find_element_by_id(self.search_textbox_id).clear()
        self.driver.find_element_by_id(self.search_textbox_id).send_keys(item)

    def click_search_icon(self):
        self.driver.find_element_by_class_name(self.search_button_class).click()

    def user_input_and_click_search(self, item):
        self.wait_homepage_load()
        self.search_item(item)
        self.click_search_icon()
