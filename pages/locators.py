from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    L_FORM = (By.CSS_SELECTOR, '#login_form')
    R_FORM = (By.CSS_SELECTOR, '#register_form')
    R_FORM_email = (By.ID, 'id_registration-email')
    R_FORM_pass1 = (By.ID, 'id_registration-password1')
    R_FORM_pass2 = (By.ID, 'id_registration-password2')
    R_FORM_submit = (By.NAME, 'registration_submit')


class ProductPageLocators:
    buy_btn = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    desc_table = (By.CLASS_NAME, 'table.table-striped')
    price = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[1]')
    success_buy = (
        By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade.in')
    title = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    alert_title = (By.CSS_SELECTOR, '#messages strong')
    alert_price = (
        By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]/div/p/strong')
    SUCCESS_MESSAGE = (
        By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade.in')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    basket = (
        By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]/span/a')
    basket_items = (By.ID, 'basket_formset')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")