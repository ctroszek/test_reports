from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_click_sign_button(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()