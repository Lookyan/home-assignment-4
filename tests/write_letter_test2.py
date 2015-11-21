from time import sleep
import unittest
from login_page import LoginPage
from compose_page import ComposePage

from selenium import webdriver


class WriteLetterTest2(unittest.TestCase):
    EMAIL = 'lewn01'
    PASSWORD = 'abcd12345'

    def setUp(self):
        self.driver = webdriver.Firefox()

        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.form()
        login_form.set_email_name(self.EMAIL)
        login_form.set_password(self.PASSWORD)
        login_form.submit()

        self.compose_page = ComposePage(self.driver)
        self.compose_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_copy_to_appear(self):
        header_switcher = self.compose_page.header_switcher()
        header_switcher.get_dropdown_button().click()
        header_switcher.get_dropdown_list_element(header_switcher.DROPDOWN_LIST_HIDDEN_COPY).click()
        # sleep(5)
        header_switcher.get_dropdown_list_element(header_switcher.DROPDOWN_LIST_HIDDEN_COPY).click()