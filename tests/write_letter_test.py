import unittest
from login_page import LoginPage
from compose_page import ComposePage
from addressbook_page import AddressBookPage
from addressbook_add_page import AddressBookAddPage

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
        res = self.choose_by_js('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)


    #1.4.1.1
    def test_pick_all_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.pick_emails('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #1.4.1.2
    def test_pick_starred_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.pick_starred()
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #1.4.1.3
    def test_pick_and_unpick_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.pick_unpick('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(not res)

    #1.4.2
    def test_add_contact_from_address_book(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.add_contact('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #1.4.5.1
    def test_search_by_fio(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.search_fio('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #1.4.5.2
    def test_contacts_search(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.search_email('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #1.4.6
    def test_contact_pick_by_search(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.search_and_pick('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #1.4.7
    def test_number_of_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.number_of_cont('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

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
        
    #2.3
    def test_choose_contact_js_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.choose_by_js('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)


    #2.4.1.1
    def test_pick_all_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.pick_emails('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #2.4.1.2
    def test_pick_starred_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.pick_starred()
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #2.4.1.3
    def test_pick_and_unpick_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.pick_unpick('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(not res)

    #2.4.2
    def test_add_contact_from_address_book_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.add_contact('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #2.4.5.1
    def test_search_by_fio_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.search_fio('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #2.4.5.2
    def test_contacts_search_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.search_email('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #2.4.6
    def test_contact_pick_by_search_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.search_and_pick('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    #2.4.7
    def test_number_of_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.add_contact("Test1", "Test1", "test1@mail.ru", "")
        res = self.number_of_cont('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

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
    def test_hidden_copy_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))

    #3.2
    def test_hidden_copy_incorrect_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_wrong_email())

    #3.6
    def test_hidden_copy_correct_incorrect(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_hidden_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))
        self.assertTrue(letter_params.is_span_wrong_email())

    #3.7
    def test_hidden_copy_equal_emails(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        self.assertEqual(1, letter_params.count_emails("test@mail.ru"))

    #3.8
    def test_hidden_copy_addr_removal(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.remove_email("test@mail.ru")
        self.assertTrue(letter_params.check_email_removal("test@mail.ru"))

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


    #helper funcs:

    def choose_by_js(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.choose_contact("test1@mail.ru", type_field)
        res = letter_params.is_span_right_email("Test1 Test1")
        letter_params.remove_email_any("test1@mail.ru")
        letter_params.leave_confirm_off()
        return res

    def pick_emails(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.pick_all_emails()
        res = letter_params.is_email_selected()
        letter_params.leave_confirm_off()
        return res

    def pick_starred(self, type_field):
        self.address_book_page.open()
        toolbar = self.address_book_page.toolbar()
        toolbar.star_contact("test1@mail.ru")
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.pick_starred_emails()
        letter_params.pick_all_emails()
        res = letter_params.is_email_selected()
        letter_params.leave_confirm_off()
        return res

    def pick_unpick(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.pick_all_emails()
        letter_params.pick_all_emails()
        res = letter_params.is_email_selected()
        letter_params.leave_confirm_off()
        return res

    def add_contact(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.pick_by_email('test1@mail.ru')
        letter_params.click_add_contact()
        letter_params.switch_to_main_window()
        res = letter_params.is_span_right_email("test1@mail.ru")
        letter_params.leave_confirm_off()
        return res

    def search_fio(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.search_contact("Test1 Test1")
        res = letter_params.is_results_found()
        return res

    def search_email(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.search_contact("test1@mail.ru")
        res = letter_params.is_results_found()
        return res

    def number_of_cont(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        res = letter_params.number_of_contacts()
        return res

    def search_and_pick(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.search_contact("Test1 Test1")
        letter_params.pick_by_email("test1@mail.ru")
        letter_params.click_add_contact()
        letter_params.switch_to_main_window()
        res = letter_params.is_span_right_email("test1@mail.ru")
        letter_params.leave_confirm_off()
        return res