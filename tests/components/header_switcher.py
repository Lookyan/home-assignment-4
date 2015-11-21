# coding=UTF-8

from tests.base import Component


class HeaderSwitcher(Component):
    BASE = "//div[@class='compose__header__switcher']"
    DROPDOWN_BUTTON = BASE + "//div[contains(@class, 'dropdown__checkbox')]"
    DROPDOWN_LIST = BASE + "//div[contains(@class, 'dropdown__list')]"
    DROPDOWN_LIST_ELEMENT = DROPDOWN_LIST + "/div[@data-type='{}']"
    COPY = 'CC'
    HIDDEN_COPY = 'BCC'
    FROM = 'From'
    NOTIFY_READ = 'Receipt'
    PRIORITY = 'Priority'
    NO_REPLY = 'Notify'
    ROW_BIG = "//div[contains(@class, 'compose__header__row_{}')]"
    ROW_SMALL = "//span[contains(@class, 'js-row-{}')]"
    NO_REPLY_DROPDOWN_BTN = "//div[contains(@class, 'js-dropdown-select-notify')]"
    NO_REPLY_DROPDOWN_BTN_TEXT = NO_REPLY_DROPDOWN_BTN + "//span[@class='dropdown__button-inline__text']"
    NO_REPLY_DROPDOWN_LIST_ELEM = NO_REPLY_DROPDOWN_BTN + "//div[contains(@class, 'dropdown__list__item') and @data-time='{}']"

    # def __init__(self, driver):
    #     Component.__init__(self, driver)
    #     self.dropdown_button = self.driver.find_element_by_xpath(self.DROPDOWN_BUTTON)

    def get_dropdown_button(self):
        return self.driver.find_element_by_xpath(self.DROPDOWN_BUTTON)

    def get_dropdown_list_element(self, elem):
        return self.driver.find_element_by_xpath(self.DROPDOWN_LIST_ELEMENT.format(elem))

    def get_row(self, row):
        if row in (self.COPY, self.HIDDEN_COPY, self.FROM):
            return self.driver.find_element_by_xpath(self.ROW_BIG.format(row.lower()))
        else:
            return self.driver.find_element_by_xpath(self.ROW_SMALL.format(row))

    def get_no_reply_dropdown_btn(self):
        return self.driver.find_element_by_xpath(self.NO_REPLY_DROPDOWN_BTN)

    def get_no_reply_dropdown_btn_text(self):
        return self.driver.find_element_by_xpath(self.NO_REPLY_DROPDOWN_BTN_TEXT).text

    def get_no_reply_dropdown_list_elem(self, time):
        return self.driver.find_element_by_xpath(self.NO_REPLY_DROPDOWN_LIST_ELEM.format(time))