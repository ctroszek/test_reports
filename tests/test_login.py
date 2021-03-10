from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.main_page import MainPage


def test_user_login(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()
    login_page.login('dmitry@gmail.com', '11111')
    account_page = AccountPage(browser)
    account_page.should_be_account_page()

