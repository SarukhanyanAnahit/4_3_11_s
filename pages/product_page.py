from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def add_product_to_basket(self, timeout=10):
        button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(ProductPageLocators.add_bsk)
        )
        button.click()
    def should_be_product_added_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.prod_name).text
        message_name = self.browser.find_element(*ProductPageLocators.name_in_message).text
        assert product_name == message_name

    def should_be_basket_price_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.prod_price).text
        basket_price = self.browser.find_element(*ProductPageLocators.total_message).text
        assert product_price == basket_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)