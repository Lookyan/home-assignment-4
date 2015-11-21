# coding=UTF-8

from tests.base import Component


class HeaderSwitcher(Component):
    BASE = "//div[@class='compose__header__switcher']"
    DROPDOWN_BUTTON = BASE + "//div[contains(@class, 'dropdown__checkbox')]"
    DROPDOWN_LIST = BASE + "//div[contains(@class, 'dropdown__list')]"
    DROPDOWN_LIST_ELEMENT = DROPDOWN_LIST + "/div[@data-type='{}']"
    DROPDOWN_LIST_COPY = 'CC'
    DROPDOWN_LIST_HIDDEN_COPY = 'BCC'
    DROPDOWN_LIST_FROM = 'From'
    DROPDOWN_LIST_NOTIFY_READ = 'Receipt'
    DROPDOWN_LIST_PRIORITY = 'Priority'
    DROPDOWN_LIST_NOTIFY_NOREPLY = 'Notify'

    def __init__(self, driver):
        Component.__init__(self, driver)
        self.dropdown_button = self.driver.find_element_by_xpath(self.DROPDOWN_BUTTON)

    def get_dropdown_button(self):
        return self.dropdown_button

    def get_dropdown_list_element(self, elem):
        return self.driver.find_element_by_xpath(self.DROPDOWN_LIST_ELEMENT.format(elem))