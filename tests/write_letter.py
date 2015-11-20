import unittest
from login import LoginPage
from compose import ComposePage

from selenium import webdriver


class WriteLetterTest(unittest.TestCase):
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

    def tearDown(self):
        self.driver.quit()

    def test_reciever_field(self):
        compose_page = ComposePage(self.driver)
        compose_page.open()
        letter_params = compose_page.letter_params()
        TEST_LEGAL_EMAIL = "test@mail.ru"
        letter_params.set_reciever_address(TEST_LEGAL_EMAIL)
        text = letter_params.is_span_right_email(TEST_LEGAL_EMAIL)