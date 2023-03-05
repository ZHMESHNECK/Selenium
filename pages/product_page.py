from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    def should_be_object_page(self):
        self.check_buy_btn()
        self.check_desc_table()
        self.check_price()

    def buy_items(self):
        link = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.buy_btn))
        link.click()

    # проверка присутствия кнопки покупки
    def check_buy_btn(self):
        assert self.is_element_present(
            *ProductPageLocators.buy_btn), 'buy button isn`t presented'

    # наличие описания товара
    def check_desc_table(self):
        assert self.is_element_present(
            *ProductPageLocators.desc_table), 'description table isn`t presented'

    # присутствие цены
    def check_price(self):
        assert self.is_element_present(
            *ProductPageLocators.price), 'price isn`t presented'

    # проверка успешности покупки
    def check_success_buy(self):
        assert self.is_element_present(
            *ProductPageLocators.success_buy), 'success alert isn`t presented'

    # проверка назв. книги в алерте и заголовке
    def check_allert_succ(self):
        title_1 = self.browser.find_element(*ProductPageLocators.title)
        title_1_text = title_1.text
        title_2 = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.alert_title))
        title_2 = self.browser.find_element(*ProductPageLocators.alert_title)
        assert title_1_text == title_2.text, 'success alert has another named of title'

    def check_price_Basket_total(self):
        price = self.browser.find_element(*ProductPageLocators.price)
        price_text = price.text
        price_2 = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.alert_price))
        assert price_text == price_2.text, 'different prices'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_wait_hide_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
