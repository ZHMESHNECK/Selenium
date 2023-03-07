from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

'''def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = LoginPage(browser, link)
    page.open()                      
    # page.go_to_login_page()
    page.should_be_login_page()
'''


## ! 1 способ перехода на другую страницу
'''def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()'''

## ! 2
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()