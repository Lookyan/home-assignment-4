# coding=UTF-8

from tests.base import Component
from selenium.webdriver.support.ui import WebDriverWait


class Contact(Component):

    FIRST_NAME = "//input[@name='firstname']"
    LAST_NAME = "//input[@name='lastname']"
    EMAIL = "//input[@name='emails']"
    ENABLE_GROUP = "//div[@class='form__field__labels form__field js-labels-control']"
    GROUP = "//input[@class='form__field__labels__input ac_input']"
    SAVE_BUTTON = "//div/span[contains(.,'Сохранить')]"
    CHECKBOX_EMAIL = "//div[@class='messageline contactline' and contains(., '{0}')]/label/input"
    DELETE_BUTTON = "//div[@title='Удалить']"
    DELETE_CONFIRM_BUTTON = "//button[contains(.,'Удалить')]"

    def add_contact(self, first_name, second_name, email, group_name):
        self.get_elem(self.FIRST_NAME).send_keys(first_name)
        self.get_elem(self.LAST_NAME).send_keys(second_name)
        self.get_elem(self.EMAIL).send_keys(email)
        self.driver.find_element_by_xpath(self.ENABLE_GROUP).click()
        self.get_elem(self.GROUP).send_keys(group_name)
        self.get_elem(self.SAVE_BUTTON).click()

    def get_elem(self, xpath):
        return WebDriverWait(self.driver, 30).until(lambda s: s.find_element_by_xpath(xpath))

    def delete_contact(self, email):
        self.driver.find_element_by_xpath(self.CHECKBOX_EMAIL.format(email)).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
        self.driver.find_element_by_xpath(self.DELETE_CONFIRM_BUTTON).click()
