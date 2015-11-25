# coding=UTF-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from base import Page
from components.letter_params import LetterParams
from components.header_switcher import HeaderSwitcher
from components.content_edit import ContentEdit
from components.main_toolbar import MainToolbar
from components.sent_letter import SentLetter


class ComposePage(Page):
    PATH = '/compose/'

    # def __init__(self, driver):
        # Page.__init__(self, driver)
        # self.letter_params = LetterParams(self.driver)
        # self.header_switcher = HeaderSwitcher(self.driver)

    def letter_params(self):
        return LetterParams(self.driver)

    def header_switcher(self):
        return HeaderSwitcher(self.driver)

    def content_edit(self):
        return ContentEdit(self.driver)

    def main_toolbar(self):
        return MainToolbar(self.driver)

    def sent_letter(self):
        return SentLetter(self.driver)