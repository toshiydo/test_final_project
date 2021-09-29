from .base_page import BasePage
from .locators import ProductPageLocators

class Productpage(BasePage):

    def press_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON)
        button_add_to_basket.click()

    def compare_elements(self):
        self.product_name_alert()
        self.product_price_alert()
        # self.test_guest_cant_see_success_message_after_adding_product_to_basket()
        self.test_message_disappeared_after_adding_product_to_basket()

    def product_name_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        product_name_in_trash = self.browser.find_element(*ProductPageLocators.NAME_TRASH).text
        print(product_name, product_name_in_trash)
        assert product_name == product_name_in_trash, "not correct name"
        
    def product_price_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        product_price_in_trash = self.browser.find_element(*ProductPageLocators.PRICE_TRASH).text
        print(product_price, product_price_in_trash)
        assert product_price == product_price_in_trash, "not correct price"
        

    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


    def test_guest_cant_see_success_message_after_adding_product_to_basket(self): 
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "is_not_element_present message is presented, but should not be"

    def test_guest_cant_see_success_message(self): 
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "NO BASKET!!!is_not_element_present message is presented, but should not be"
        

    def test_message_disappeared_after_adding_product_to_basket(self): 
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "is_disappeared message is presented, but should not be"
        
     


