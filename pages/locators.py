from selenium.webdriver.common.by import By

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_EMAIL_ADDRESS = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class BasketPageLocators():
    BASKET = (By.CSS_SELECTOR, "span.btn-group a")
    NO_ITEM = (By.XPATH, "//div[@class='basket-items']")
    TEXT = (By.XPATH, "//*[@id='content_inner']/p")
 
class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_PRODUCT_IN_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")