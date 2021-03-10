from selenium.webdriver.common.by import By


class BasketPageLocator:

    LOCATOR_BASKET_TEXT = (By.CLASS_NAME, 'page-heading')
    LOCATOR_BUTTON_BASKET = (
        By.XPATH,
        '//a[@href="http://automationpractice.com/index.php?controller=order"]'
    )
    LOCATOR_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '.alert.alert-warning')
