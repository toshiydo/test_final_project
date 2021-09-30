from .locators import BasketPageLocators
from .base_page import BasePage
from selenium import webdriver
class BasketPage(BasePage):
    def no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_PRODUCT_IN_BASKET), "product in basket"

    def have_text_in_basket(self):
        assert 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text, "no TEXT"