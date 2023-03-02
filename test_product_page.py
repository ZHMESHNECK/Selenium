from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_object_page()
    page.buy_items()
    page.solve_quiz_and_get_code()
    page.check_allert_succ()
    
    time.sleep(10)
    
