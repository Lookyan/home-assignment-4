# coding=UTF-8

from base import Page
from components.contact import Contact


class AddressBookAddPage(Page):
    PATH = '/addressbook/add'

    def contact(self):
        return Contact(self.driver)