import unittest
from login_page import LoginPage
from compose_page import ComposePage
from time import sleep

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

        self.compose_page = ComposePage(self.driver)
        self.compose_page.open()

    def tearDown(self):
        self.driver.quit()

    #1.1
    def test_receiver_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))

    #1.2
    def test_receiver_field_wrong_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_wrong_email())

    #1.3
    #1.4

    #1.5
    def test_correct_incorrect_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.set_to_addr("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_right_email())
        self.assertTrue(letter_params.is_span_wrong_email())

    #1.6
    def test_enter_equal_emails(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        self.assertEqual(1, letter_params.count_emails("test@mail.ru"))
