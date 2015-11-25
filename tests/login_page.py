# coding=UTF-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

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
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.EMAIL)))
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(email)

    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.PASS)))
        self.driver.find_element_by_xpath(self.PASS).send_keys(password)

    def submit(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.SUBMIT)))
        self.driver.find_element_by_xpath(self.SUBMIT).click()

