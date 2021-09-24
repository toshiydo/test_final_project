from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "input[id='id_login-username']")
    REGISTER_FORM = (By.CSS_SELECTOR, "input[id='id_registration-email']")
    