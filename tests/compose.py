# coding=UTF-8

from page import Page, Component
from selenium.webdriver.support.ui import WebDriverWait


class ComposePage(Page):
    PATH = '/compose/'

    def letter_params(self):
        return LetterParams(self.driver)

class LetterParams(Component):
    RECIEVER_ADDRESS = "//textarea[@data-original-name='To']"
    SPAN_LEGAL_EMAIL = "//span[@class='js-compose-label compose__labels__label']"

    def set_reciever_address(self, address):
        self.driver.find_element_by_xpath(self.RECIEVER_ADDRESS).send_keys(address + " ")

    def is_span_right_email(self, address):
        return self.driver.find_element_by_xpath(self.SPAN_LEGAL_EMAIL).text
        # return WebDriverWait(self.driver, 30, 0.1).until(
        #     lambda d: d.find_element_by_xpath(self.SPAN_LEGAL_EMAIL).text
        # )