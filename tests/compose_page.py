# coding=UTF-8

from base import Page
from components.letter_params import LetterParams
from components.header_switcher import HeaderSwitcher


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