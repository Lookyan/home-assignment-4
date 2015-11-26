# coding=UTF-8

from tests.base import Component


class LetterList(Component):

    LETTER_SELECT_CHECKBOX = "//div[@data-mnemo='letters']" \
                             "//div[@data-bem='b-datalist__item' and .//div[contains(@class, 'b-datalist__item__subj')]/span[contains(text(), 'hahaha')]]" \
                             "//div[contains(@class, 'js-item-checkbox')]"
    REMOVE_LETTER_BTN = "//div[@data-name='remove']"

    def delete_letter_with_text(self, text):
        self.driver.find_element_by_xpath(self.LETTER_SELECT_CHECKBOX.format(text)).click()
        self.driver.find_element_by_xpath(self.REMOVE_LETTER_BTN).click()