from locator.basket_page_locator import BasketPageLocator
from pages.base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.basket_text_is_present()

    def basket_text_is_present(self):
        basket_text = self.find_element(
            BasketPageLocator.LOCATOR_BASKET_TEXT
        ).text
        assert basket_text == 'SHOPPING-CART SUMMARY'

    def basket_is_empty(self):
        basket_empty = self.find_element(
            BasketPageLocator.LOCATOR_BASKET_IS_EMPTY
        ).text
        assert basket_empty == 'Your shopping cart is empty.'
