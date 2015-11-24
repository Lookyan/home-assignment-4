# coding=UTF-8

from base import Page
from components.letter_list import LetterList


class TemplatesPage(Page):
    PATH = '/messages/templates/'

    def letter_list(self):
        return LetterList(self.driver)