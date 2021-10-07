from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_ITEM), "Some item in basket now!"

    def basket_text_is_null(self):
        assert "Your basket is empty." in self.is_element_text(*BasketPageLocators.TEXT), "No text"