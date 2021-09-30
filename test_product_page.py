# from pages.product_page import Productpage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
import time
import pytest

urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"]

# @pytest.mark.xfail(reason="fixing this bug right now")        
# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = Productpage(browser, link)
#     page.open()
#     # page.test_guest_cant_see_success_message()      #второй
#     page.press_button_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.compare_elements()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = Productpage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = Productpage(browser, link)
#     page.open()
#     page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = MainPage(browser, link)
        page.open()
        page.product_in_basket_opened_from_main_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.no_product_in_basket()
        basket_page.have_text_in_basket()
    
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"