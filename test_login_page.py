from pages.login_page import LoginPage


def test_guest_can_see_login_page(browser):
    link = "https://the-internet.herokuapp.com/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
