from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class ProductPageLocators():
    add_bsk=(By.XPATH, '//button[@value="Add to basket"]')
    prod_name = (By.CSS_SELECTOR, ".product_main h1")
    prod_price = (By.XPATH, '//p[@class="price_color"]')
    name_in_message = (By.XPATH, '//div[@class="alertinner "]/strong')
    total_message = (By.XPATH, '(//div[@class="alertinner "])[3]/p/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class MainPageLocators():
   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
   login_form = (By.ID, "login_form")
   register_form = (By.ID, "register_form")
