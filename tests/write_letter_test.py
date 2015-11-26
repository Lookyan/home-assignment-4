# -*- coding: utf-8 -*-

import unittest
import os
from login_page import LoginPage
from compose_page import ComposePage
from addressbook_page import AddressBookPage
from addressbook_add_page import AddressBookAddPage
from components.header_switcher import HeaderSwitcher
from selenium.webdriver import DesiredCapabilities, Remote
from drafts_page import DraftsPage

from selenium import webdriver


class WriteLetterTest(unittest.TestCase):
    EMAIL = os.environ['TTHA4LOGIN']
    PASSWORD = os.environ['TTHA4PASSWORD']
    BROWSER = os.environ['TTHA4BROWSER']

    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.BROWSER).copy()
        )

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

        self.header_switcher = self.compose_page.header_switcher()
        self.header_switcher_dropdown_btn = self.header_switcher.get_dropdown_button()

        self.content_edit = self.compose_page.content_edit()

    def tearDown(self):
        self.driver.quit()


    def test_receiver_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))

    def test_receiver_field_wrong_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_wrong_email())

    def test_choose_contact_js(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.choose_by_js('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)


    def test_pick_all_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_picked_emails('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_pick_starred_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_pick_starred('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_pick_and_unpick_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_pick_unpicked('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(not res)

    def test_add_contact_from_address_book(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_contact_added('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_search_by_fio(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_search_fio_appears('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_contacts_search(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_search_email_found('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_contact_pick_by_search(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_search_and_picked('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_number_of_contacts(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_number_of_cont_equal('To')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_correct_incorrect_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.set_to_addr("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))
        self.assertTrue(letter_params.is_span_wrong_email())

    def test_enter_equal_emails(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        self.assertEqual(1, letter_params.count_emails("test@mail.ru"))

    def test_email_remove(self):
        letter_params = self.compose_page.letter_params()
        letter_params.set_to_addr("test@mail.ru")
        letter_params.unfocus()
        letter_params.remove_email("test@mail.ru")
        self.assertTrue(letter_params.check_email_removal("test@mail.ru"))

    def test_copy_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))

    def test_copy_incorrect_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_wrong_email())

    def test_choose_contact_js_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.choose_by_js('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_pick_all_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_picked_emails('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_pick_starred_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_pick_starred('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_pick_and_unpick_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_pick_unpicked('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(not res)

    def test_add_contact_from_address_book_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_contact_added('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_search_by_fio_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_search_fio_appears('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_contacts_search_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_search_email_found('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_contact_pick_by_search_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_search_and_picked('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_number_of_contacts_cc(self):
        self.address_book_add_page.open()
        contact = self.address_book_add_page.contact()
        contact.is_contact_added("Test1", "Test1", "test1@mail.ru", "")
        res = self.is_number_of_cont_equal('CC')
        self.address_book_page.open()
        contact.delete_contact("test1@mail.ru")
        self.assertTrue(res)

    def test_copy_correct_incorrect(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))
        self.assertTrue(letter_params.is_span_wrong_email())

    def test_copy_equal_emails(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        self.assertEqual(1, letter_params.count_emails("test@mail.ru"))

    def test_copy_addr_removal(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.remove_email("test@mail.ru")
        self.assertTrue(letter_params.check_email_removal("test@mail.ru"))

    def test_hidden_copy_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))

    def test_hidden_copy_incorrect_email(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_wrong_email())

    def test_hidden_copy_correct_incorrect(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_hidden_copy_email("wrongemail.ru")
        letter_params.unfocus()
        self.assertTrue(letter_params.is_span_right_email("test@mail.ru"))
        self.assertTrue(letter_params.is_span_wrong_email())

    def test_hidden_copy_equal_emails(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        self.assertEqual(1, letter_params.count_emails("test@mail.ru"))

    def test_hidden_copy_addr_removal(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_hidden_copy_email("test@mail.ru")
        letter_params.unfocus()
        letter_params.remove_email("test@mail.ru")
        self.assertTrue(letter_params.check_email_removal("test@mail.ru"))

    def test_focus_via_topic_click(self):
        letter_params = self.compose_page.letter_params()
        letter_params.click_topic_for_focus()
        self.assertTrue(letter_params.check_focus_on_topic_input())

    def test_topic_field(self):
        letter_params = self.compose_page.letter_params()
        letter_params.enter_topic("Lorem ipsum")
        self.assertTrue(letter_params.check_topic_text("Lorem ipsum"))

    def test_copy_header_toggle(self):
        header = self.header_switcher.get_row(self.header_switcher.COPY)
        dropdown_elem = self.header_switcher.get_dropdown_list_element(self.header_switcher.COPY)
        is_visible = header.is_displayed()

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), not is_visible)

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), is_visible)

    def test_hidden_copy_header_toggle(self):
        header = self.header_switcher.get_row(self.header_switcher.HIDDEN_COPY)
        dropdown_elem = self.header_switcher.get_dropdown_list_element(self.header_switcher.HIDDEN_COPY)
        is_visible = header.is_displayed()

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), not is_visible)

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), is_visible)

    def test_from_header_toggle(self):
        header = self.header_switcher.get_row(self.header_switcher.FROM)
        dropdown_elem = self.header_switcher.get_dropdown_list_element(self.header_switcher.FROM)
        is_visible = header.is_displayed()

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), not is_visible)

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), is_visible)

    def test_priority_header_toggle(self):
        header = self.header_switcher.get_row(self.header_switcher.PRIORITY)
        dropdown_elem = self.header_switcher.get_dropdown_list_element(self.header_switcher.PRIORITY)
        is_visible = header.is_displayed()

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), not is_visible)

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), is_visible)

    def test_notify_read_header_toggle(self):
        header = self.header_switcher.get_row(self.header_switcher.NOTIFY_READ)
        dropdown_elem = self.header_switcher.get_dropdown_list_element(self.header_switcher.NOTIFY_READ)
        is_visible = header.is_displayed()

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), not is_visible)

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), is_visible)

    def test_no_reply_header_toggle(self):
        header = self.header_switcher.get_row(self.header_switcher.NO_REPLY)
        dropdown_elem = self.header_switcher.get_dropdown_list_element(self.header_switcher.NO_REPLY)
        is_visible = header.is_displayed()

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), not is_visible)

        self.header_switcher_dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), is_visible)

    def test_change_notify_time(self):
        header_switcher = self.compose_page.header_switcher()
        notify_header = header_switcher.get_row(HeaderSwitcher.NO_REPLY)

        if not notify_header.is_displayed():
            header_switcher.get_dropdown_button().click()
            header_switcher.get_dropdown_list_element(HeaderSwitcher.NO_REPLY).click()

        header_switcher.get_no_reply_dropdown_btn().click()
        header_switcher.get_no_reply_dropdown_list_elem(3600).click()
        self.assertEqual(header_switcher.get_no_reply_dropdown_btn_text(), u'1 час')

    #################################################

    def test_add_content(self):
        text = u"hi hi hi"
        self.content_edit.change_text(text)
        self.assertEqual(self.content_edit.get_text(), text)

    def test_remove_content(self):
        text = u"hi hi hi"
        num = 3
        self.content_edit.change_text(text)
        self.content_edit.send_backspaces(num)
        self.assertEqual(self.content_edit.get_text(), text[:-num])

    def test_bold(self):
        self.content_edit.change_text("lalala")
        self.content_edit.add_simple_style("bold")
        self.assertTrue(self.content_edit.check_bold())

    def test_italic(self):
        self.content_edit.change_text("lalala")
        self.content_edit.add_simple_style("italic")
        self.assertTrue(self.content_edit.check_italic())

    def test_underline(self):
        self.content_edit.change_text("lalala")
        self.content_edit.add_simple_style("underline")
        self.assertTrue(self.content_edit.check_underline())

    def test_text_color(self):
        color = "#89f641"
        self.content_edit.change_text("lalala")
        self.content_edit.add_text_color(color)
        self.assertTrue(self.content_edit.check_text_color(color))

    def test_background_color(self):
        color = "#89f641"
        self.content_edit.change_text("lalala")

        self.content_edit.add_background_color(color)
        self.assertTrue(self.content_edit.check_background_color(color))

    def test_font_size_family(self):
        self.content_edit.change_text("lalala")

        family = "comic sans"
        self.content_edit.pick_font_family(family)
        self.assertTrue(self.content_edit.check_font_family(family))

        family = "arial black"
        self.content_edit.pick_font_family(family)
        self.assertTrue(self.content_edit.check_font_family(family))

        family = "georgia"
        self.content_edit.pick_font_family(family)
        self.assertTrue(self.content_edit.check_font_family(family))

        size = 5
        self.content_edit.pick_font_size(size)
        self.assertTrue(self.content_edit.check_font_size(size))

        size = 2
        self.content_edit.pick_font_size(size)
        self.assertTrue(self.content_edit.check_font_size(size))

    def test_align(self):
        self.content_edit.change_text("lalala")

        align = "center"
        self.content_edit.add_align(align)
        self.assertTrue(self.content_edit.check_align(align))

        align = "right"
        self.content_edit.add_align(align)
        self.assertTrue(self.content_edit.check_align(align))

        align = "left"
        self.content_edit.add_align(align)
        self.assertTrue(self.content_edit.check_align(align))

    def test_indent(self):
        self.content_edit.change_text("lalala")

        self.content_edit.add_indent()
        self.assertTrue(self.content_edit.check_indent(1))

        self.content_edit.add_indent()
        self.assertTrue(self.content_edit.check_indent(2))

        self.content_edit.remove_indent()
        self.content_edit.remove_indent()
        self.assertTrue(self.content_edit.check_indent(0))

    def test_list_ordered(self):
        self.content_edit.change_text("lalala")

        order = 'ordered'
        self.content_edit.add_list(order)
        self.assertTrue(self.content_edit.check_list(order))

        self.content_edit.add_text("\nhahaha")
        self.assertTrue(self.content_edit.check_list(order, 2))

    def test_list_unordered(self):
        self.content_edit.change_text("lalala")

        order = 'unordered'
        self.content_edit.add_list(order)
        self.assertTrue(self.content_edit.check_list(order))

        self.content_edit.add_text("\nhahaha")
        self.assertTrue(self.content_edit.check_list(order, 2))

    def test_emotion(self):
        self.content_edit.add_emotion('drinks')
        self.assertTrue(self.content_edit.check_emotion('drinks'))

    def test_undo_redo(self):
        text = 'lalala'
        self.content_edit.change_text(text)

        self.content_edit.undo()
        self.assertEqual(self.content_edit.get_text(), '')
        self.content_edit.redo()
        self.assertEqual(self.content_edit.get_text(), text)

    def test_add_line(self):
        self.content_edit.add_line()
        self.content_edit.check_line()

    def test_add_link(self):
        href = 'http://mail.ru'
        title = 'MailRu'
        self.content_edit.add_link(href, title)
        self.content_edit.check_link(href, title)

    def test_translit(self):
        text = u'привет'
        translited = 'privet'
        self.content_edit.change_text(text)
        self.content_edit.translit_text()
        self.assertEqual(self.content_edit.get_text(), translited)

    def test_remove_format(self):
        text = 'hihihi'
        self.content_edit.change_text(text)
        self.content_edit.add_simple_style('bold')
        self.content_edit.add_simple_style('italic')
        self.assertNotEqual(self.content_edit.check_tags(), 0)
        self.content_edit.remove_format()
        self.assertEqual(self.content_edit.check_tags(), 0)

    def test_toolbar_toogle(self):
        self.content_edit.minimize_toolbar()
        self.assertEqual(self.content_edit.check_toolbar(), 'small')

        self.content_edit.maximize_toolbar()
        self.assertEqual(self.content_edit.check_toolbar(), 'big')

    def test_theme_add_delete(self):
        theme = 1
        self.content_edit.pick_theme(theme)
        self.assertTrue(self.content_edit.check_theme(theme))

        self.content_edit.delete_theme()
        self.assertFalse(self.content_edit.check_theme(theme))

    def test_card_add_delete(self):
        card = 1
        self.content_edit.pick_card(card)
        self.assertTrue(self.content_edit.check_card(card))

        self.content_edit.delete_card()
        self.assertFalse(self.content_edit.check_card(card))

    def test_spelling(self):
        self.content_edit.change_text(u'привет')
        self.assertTrue(self.content_edit.check_spelling())

    def test_translate(self):
        self.content_edit.change_text(u'привет')
        self.content_edit.translate()
        self.assertEqual(self.content_edit.get_text(), 'hi')

    def test_virtual_keyb(self):
        self.content_edit.clear_edit()
        self.content_edit.virtual_keyboard_type(u'привет')
        self.assertEqual(self.content_edit.get_text(), u'привет')

    def test_cancel(self):
        self.content_edit.change_text("lalala")
        self.assertTrue(self.compose_page.main_toolbar().cancel())

    def test_save_letter(self):
        text = 'lalala'
        self.content_edit.change_text(text)
        main_toolbar = self.compose_page.main_toolbar()
        main_toolbar.save()
        self.assertTrue(main_toolbar.check_saved())

        drafts_page = DraftsPage(self.driver)
        drafts_page.open()
        drafts_page.letter_list().delete_letter_with_text(text)

    def test_send_letter(self):
        self.content_edit.change_text("lalala")
        self.compose_page.letter_params().set_to_addr("bit-bucket@test.smtp.org")
        self.compose_page.main_toolbar().send()
        self.assertTrue(self.compose_page.sent_letter().check_sent_letter())


    #helper funcs:

    def choose_by_js(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.choose_contact("test1@mail.ru", type_field)
        res = letter_params.is_span_right_email("Test1 Test1")
        letter_params.remove_email_any("test1@mail.ru")
        letter_params.leave_confirm_off()
        return res

    def is_picked_emails(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.pick_all_emails()
        res = letter_params.is_email_selected()
        letter_params.leave_confirm_off()
        return res

    def is_pick_starred(self, type_field):
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

    def is_pick_unpicked(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.pick_all_emails()
        letter_params.pick_all_emails()
        res = letter_params.is_email_selected()
        letter_params.leave_confirm_off()
        return res

    def is_contact_added(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.pick_by_email('test1@mail.ru')
        letter_params.click_add_contact()
        letter_params.switch_to_main_window()
        res = letter_params.is_span_right_email("test1@mail.ru")
        letter_params.leave_confirm_off()
        return res

    def is_search_fio_appears(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.search_contact("Test1 Test1")
        res = letter_params.is_results_found()
        return res

    def is_search_email_found(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        letter_params.search_contact("test1@mail.ru")
        res = letter_params.is_results_found()
        return res

    def is_number_of_cont_equal(self, type_field):
        self.compose_page.open()
        letter_params = self.compose_page.letter_params()
        letter_params.click_address_book(type_field)
        res = letter_params.number_of_contacts()
        return res

    def is_search_and_picked(self, type_field):
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