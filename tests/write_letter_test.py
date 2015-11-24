import unittest
from login_page import LoginPage
from compose_page import ComposePage
from addressbook_page import AddressBookPage
from addressbook_add_page import AddressBookAddPage
from selenium.webdriver.remote.errorhandler import NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
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

        self.address_book_page = AddressBookPage(self.driver)
        self.address_book_add_page = AddressBookAddPage(self.driver)

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
    def test_choose_contact_js(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.choose_contact("test1@mail.ru", 'To')
        res = letter_params.is_span_right_email("Test1 Test1")
        letter_params.remove_email_any("test1@mail.ru")
        letter_params.leave_confirm_off()
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)


    #1.4.1
    def test_choose_contact_new_window(self):
        self.address_book_page.open()
        toolbar = self.address_book_page.toolbar()
        toolbar.new_group("test")

        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "test")

        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        toolbar.group_delete("test")

    def test_address_add_open(self):
        self.address_book_add_page.open()
        sleep(100)


    #1.5
    def test_correct_incorrect_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.set_to_addr("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))
        self.assertTrue(letter_params.is_span_wrong_email())

    #1.7
    def test_enter_equal_emails(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        self.assertEqual(1, letter_params.count_emails("test@mail.ru"))

    #1.8
    def test_email_remove(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.remove_email("test@mail.ru")
        self.assertTrue(letter_params.check_email_removal("test@mail.ru"))

    #2.1
    def test_copy_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))

    #2.2
    def test_copy_incorrect_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_wrong_email())

    #2.6
    def test_copy_correct_incorrect(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))
        self.assertTrue(letter_params.is_span_wrong_email())

    #2.7
    def test_copy_equal_emails(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        self.assertEqual(1, letter_params.count_emails("test@mail.ru"))

    #2.8
    def test_copy_addr_removal(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.remove_email("test@mail.ru")
        self.assertTrue(letter_params.check_email_removal("test@mail.ru"))

    #3.1

    #4.1
    def test_focus_via_topic_click(self):
        letter_params = self.compose_page.letter_params()
        letter_params.click_topic_for_focus()
        self.assertTrue(letter_params.check_focus_on_topic_input())

    #4.2
    def test_topic_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_topic("Lorem ipsum")
        self.assertTrue(letter_params.check_topic_text("Lorem ipsum"))