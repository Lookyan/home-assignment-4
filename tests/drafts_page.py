# coding=UTF-8

from base import Page
from components.letter_list import LetterList


class DraftsPage(Page):
    PATH = '/messages/drafts/'

    def letter_list(self):
        return LetterList(self.driver)