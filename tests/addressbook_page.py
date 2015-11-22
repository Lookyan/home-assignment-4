# coding=UTF-8

from base import Page
from components.toolbar import Toolbar


class ComposePage(Page):
    PATH = '/addressbook/'

    def toolbar(self):
        return Toolbar(self.driver)