from pages.basket_page import BasketPage
from pages.main_page import MainPage


def test_basket(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_basket_page()
    basket_page = BasketPage(browser)
    basket_page.should_be_basket_page()
    basket_page.basket_is_empty()
