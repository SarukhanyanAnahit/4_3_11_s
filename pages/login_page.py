
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import register
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'url is wrong'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "login form isn't present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "register form isn't present"

    def register_new_user(self, email, password):
        self.browser.find_element(*register.Email).send_keys(email)
        self.browser.find_element(*register.Password).send_keys(password)
        self.browser.find_element(*register.re_password).send_keys(password)
        self.browser.find_element(*register.button).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"