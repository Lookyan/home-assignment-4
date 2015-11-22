# coding=UTF-8

from tests.base import Component


class Toolbar(Component):
    ADD_BUTTON = "//span[@class='b-toolbar__btn__text b-toolbar__btn__text_pad' and text()='Добавить']"

    def click_add_button(self):
        self.driver.find_element_by_xpath(self.ADD_BUTTON).click()

    