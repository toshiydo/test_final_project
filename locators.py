from selenium.webdriver.common.by import By

class ProductPageLocators:
    BUTTON = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
    NAME_TRASH = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_TRASH = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id='messages'] .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    