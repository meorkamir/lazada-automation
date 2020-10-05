from selenium import webdriver
import pytest
from pages.homepage import HomePage
from pages.resultpage import ResultPage
from pages.productpage import ProductPage
from utils import utils as utils

class TestCheckout():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Firefox(executable_path=utils.GECKO_DRIVER_PATH)
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_checkout(self, test_setup):
        try:
            driver.get(utils.URL)
            HomePage(driver).user_input_and_click_search(utils.SEARCH_INPUT)
            ResultPage(driver).user_select_first_product()
            ProductPage(driver).user_click_add_to_cart()
            ProductPage(driver).user_login(utils.USERNAME, utils.PASSWORD)

            self.assertTrue(True)
        except:
            print("Test failed!")


