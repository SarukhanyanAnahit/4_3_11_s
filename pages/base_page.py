from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .locators import ProductPageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_login_page(self, timeout=10):
        link = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(BasePageLocators.LOGIN_LINK)
        )
        link.click()

    def go_to_basket_page(self, timeout=10):
        link = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(BasePageLocators.BASKET_LINK)
        )
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK)

    def open(self):
        self.browser.get(self.url)



    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

