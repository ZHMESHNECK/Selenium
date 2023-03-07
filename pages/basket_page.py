from .base_page import BasePage
from .base_page import BasePageLocators

class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasePageLocators.basket_items), "basket isn`t emty"