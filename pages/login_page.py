from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        assert '/login/' in get_url

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.L_FORM), 'login form isn`t presented'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.R_FORM), 'register form isn`t presented'

    def register_new_user(self, email, password):
        em = self.browser.find_element(*LoginPageLocators.R_FORM_email)
        em.send_keys(email)
        pas = self.browser.find_element(*LoginPageLocators.R_FORM_pass1)
        pas.send_keys(password)
        pas = self.browser.find_element(*LoginPageLocators.R_FORM_pass2)
        pas.send_keys('Lovoostack123')

        but = self.browser.find_element(*LoginPageLocators.R_FORM_submit)
        but.click()