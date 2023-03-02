from pages.main_page import MainPage
from pages.login_page import LoginPage
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
    time.sleep(5)
    login_page.should_be_login_page()'''
## ! 2
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()