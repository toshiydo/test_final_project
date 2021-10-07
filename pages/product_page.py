from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_product_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_equals_name_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text
        assert product_name == product_name_in_basket, "product name is not correct"
        
    def should_be_equals_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_MESSAGE).text
        assert product_price == product_price_in_basket, "product price is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is disappeared, but should not be"