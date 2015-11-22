# -*- coding: utf-8 -*-

import unittest
from login_page import LoginPage
from compose_page import ComposePage
from components.header_switcher import HeaderSwitcher

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

    def toggle_header(self, what):
        header_switcher = self.compose_page.header_switcher()
        header = header_switcher.get_row(what)
        dropdown_btn = header_switcher.get_dropdown_button()
        dropdown_elem = header_switcher.get_dropdown_list_element(what)
        is_visible = header.is_displayed()

        dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), not is_visible)

        dropdown_btn.click()
        dropdown_elem.click()
        self.assertEqual(header.is_displayed(), is_visible)

    ##############################################

    def test_copy_header_toggle(self):
        self.toggle_header(HeaderSwitcher.COPY)

    def test_hidden_copy_header_toggle(self):
        self.toggle_header(HeaderSwitcher.HIDDEN_COPY)

    def test_from_header_toggle(self):
        self.toggle_header(HeaderSwitcher.FROM)

    def test_priority_header_toggle(self):
        self.toggle_header(HeaderSwitcher.PRIORITY)

    def test_notify_read_header_toggle(self):
        self.toggle_header(HeaderSwitcher.NOTIFY_READ)

    def test_no_reply_header_toggle(self):
        self.toggle_header(HeaderSwitcher.NO_REPLY)

    def test_change_notify_time(self):
        header_switcher = self.compose_page.header_switcher()
        notify_header = header_switcher.get_row(HeaderSwitcher.NO_REPLY)

        if not notify_header.is_displayed():
            header_switcher.get_dropdown_button().click()
            header_switcher.get_dropdown_list_element(HeaderSwitcher.NO_REPLY).click()

        header_switcher.get_no_reply_dropdown_btn().click()
        header_switcher.get_no_reply_dropdown_list_elem(3600).click()
        self.assertEqual(header_switcher.get_no_reply_dropdown_btn_text(), u'1 час')

    # def test_hidden_copy_toggle(self):
    #     header_switcher = self.compose_page.header_switcher()
    #     is_visible = header_switcher.get_row(header_switcher.HIDDEN_COPY).is_displayed()
    #
    #     header_switcher.get_dropdown_button().click()
    #     header_switcher.get_dropdown_list_element(header_switcher.HIDDEN_COPY).click()
    #     self.assertEqual(header_switcher.get_row(header_switcher.HIDDEN_COPY).is_displayed(), not is_visible)
    #
    #     header_switcher.get_dropdown_button().click()
    #     header_switcher.get_dropdown_list_element(header_switcher.HIDDEN_COPY).click()
    #     self.assertEqual(header_switcher.get_row(header_switcher.HIDDEN_COPY).is_displayed(), is_visible)
    #
    # def test_from_toggle(self):
    #     header_switcher = self.compose_page.header_switcher()
    #     is_visible = header_switcher.get_row(header_switcher.FROM).is_displayed()
    #
    #     header_switcher.get_dropdown_button().click()
    #     header_switcher.get_dropdown_list_element(header_switcher.FROM).click()
    #     self.assertEqual(header_switcher.get_row(header_switcher.FROM).is_displayed(), not is_visible)
    #
    #     header_switcher.get_dropdown_button().click()
    #     header_switcher.get_dropdown_list_element(header_switcher.FROM).click()
    #     self.assertEqual(header_switcher.get_row(header_switcher.FROM).is_displayed(), is_visible)
    #
    # def test_priority_toggle(self):
    #     header_switcher = self.compose_page.header_switcher()
    #     is_visible = header_switcher.get_row(header_switcher.FROM).is_displayed()
    #
    #     header_switcher.get_dropdown_button().click()
    #     header_switcher.get_dropdown_list_element(header_switcher.FROM).click()
    #     self.assertEqual(header_switcher.get_row(header_switcher.FROM).is_displayed(), not is_visible)
    #
    #     header_switcher.get_dropdown_button().click()
    #     header_switcher.get_dropdown_list_element(header_switcher.FROM).click()
    #     self.assertEqual(header_switcher.get_row(header_switcher.FROM).is_displayed(), is_visible)