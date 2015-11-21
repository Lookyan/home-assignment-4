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

        self.header_switcher = self.compose_page.header_switcher()
        self.header_switcher_dropdown_btn = self.header_switcher.get_dropdown_button()

    def tearDown(self):
        self.driver.quit()

    # def toggle_header(self, what):
    #     header = self.header_switcher.get_row(what)
    #     dropdown_elem = self.header_switcher.get_dropdown_list_element(what)
    #     is_visible = header.is_displayed()
    #
    #     self.header_switcher_dropdown_btn.click()
    #     dropdown_elem.click()
    #     self.assertEqual(header.is_displayed(), not is_visible)
    #
    #     self.header_switcher_dropdown_btn.click()
    #     dropdown_elem.click()
    #     self.assertEqual(header.is_displayed(), is_visible)

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
        # self.toggle_header(HeaderSwitcher.HIDDEN_COPY)
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
        # self.toggle_header(HeaderSwitcher.FROM)
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
        # self.toggle_header(HeaderSwitcher.PRIORITY)
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
        # self.toggle_header(HeaderSwitcher.NOTIFY_READ)
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
        # self.toggle_header(HeaderSwitcher.NO_REPLY)
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