# -*- coding: utf-8 -*-

import unittest
from login_page import LoginPage
from compose_page import ComposePage
from components.header_switcher import HeaderSwitcher
from components.content_edit import ContentEdit

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

        self.header_switcher = self.compose_page.header_switcher()
        self.header_switcher_dropdown_btn = self.header_switcher.get_dropdown_button()

        self.content_edit = ContentEdit(self.driver)

    def tearDown(self):
        self.driver.quit()

    ##############################################

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

    ########################################

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