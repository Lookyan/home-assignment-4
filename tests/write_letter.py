import unittest
from login import LoginPage

from selenium import webdriver


class WriteLetterTest(unittest.TestCase):
    EMAIL = 'lewn01'
    PASSWORD = 'abcd12345'

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.form()
        login_form.set_email_name(self.EMAIL)
        login_form.set_password(self.PASSWORD)
        login_form.submit()
