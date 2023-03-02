from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def should_be_object_page(self):
        self.check_buy_btn()
        self.check_desc_table()
        self.check_price()

    def buy_items(self):
        link = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(ProductPageLocators.buy_btn))
        link.click()

    # проверка присутствия кнопки покупки
    def check_buy_btn(self):
        assert self.is_element_present(*ProductPageLocators.buy_btn), 'buy button isn`t presented'

    # наличие описания товара
    def check_desc_table(self):
        assert self.is_element_present(*ProductPageLocators.desc_table), 'description table isn`t presented'

    # присутствие цены
    def check_price(self):
        assert self.is_element_present(*ProductPageLocators.price), 'price isn`t presented'

    # проверка успешности покупки
    def check_success_buy(self):
        assert self.is_element_present(*ProductPageLocators.success_buy), 'success alert isn`t presented'

    # проверка назв. книги в алерте и заголовке
    def check_allert_succ(self):
        title_1 = self.browser.find_element(*ProductPageLocators.title)
        title_1_text = title_1.text
        title_2 = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(ProductPageLocators.alert_title))
        title_2 = self.browser.find_element(*ProductPageLocators.alert_title)
        assert title_1_text == title_2.text, 'success alert has another named of title'
