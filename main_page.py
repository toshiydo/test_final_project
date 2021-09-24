from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) 



