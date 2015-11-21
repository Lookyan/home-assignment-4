# coding=UTF-8

from base import Page, Component


class LoginPage(Page):
    PATH = '/login/'

    def form(self):
        return LoginForm(self.driver)


class LoginForm(Component):
    EMAIL = "//input[@name='Login']"
    PASS = "//input[@name='Password']"
    SUBMIT = '//button[contains(., "Войти в почту")]'

    def set_email_name(self, email):
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASS).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

