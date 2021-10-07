from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not url for login"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.input_text(*LoginPageLocators.REGISTER_EMAIL_ADDRESS, email)
        self.input_text(*LoginPageLocators.REGISTER_PASSWORD, password)
        self.input_text(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM, password)
        self.click_button(*LoginPageLocators.REGISTER_BUTTON)


        

