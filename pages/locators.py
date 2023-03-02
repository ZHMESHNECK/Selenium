from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    L_FORM = (By.CSS_SELECTOR, '#login_form')
    R_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    buy_btn = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    desc_table = (By.CLASS_NAME, 'table.table-striped')
    price = (By.CLASS_NAME, 'price_color')
    success_buy = (By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade.in')
    title = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    alert_title = (By.CSS_SELECTOR, '#messages strong')
