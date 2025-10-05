
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
def test_guest_can_see_login_page(browser):
    link = "https://the-internet.herokuapp.com/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

@pytest.mark.reg
def test_user_can_register(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.register_new_user("example@mail.ru", "strongpassword123")


@pytest.mark.need_review
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



