# coding=UTF-8

from tests.base import Component
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.errorhandler import StaleElementReferenceException
from selenium.webdriver.remote.errorhandler import NoSuchElementException


class Toolbar(Component):
    ADD_BUTTON = "//div[@data-name='add']"
    CREATE_GROUP = "//a[contains(., 'Создать группу')]"
    GROUP_INPUT = "//input[@id='label']"
    CREATE_GROUP_BUTTON = "//span[contains(., 'Создать')]"
    SIDEBAR_GROUP = "//a/span[text()='{0}']"
    GROUP_SETTINGS_BUTTON = "//i[contains(@class, 'icon_menu_addressbook_edit')]"
    DELETE_LINK = "//a[contains(., 'Удалить')]"
    CONFIRM_DELETE_BUTTON = "//form/div[@class='popup__controls']/button[@class='btn btn_main confirm-ok']/span[@class='btn__text' and contains(., 'Удалить')]"

    def new_group(self, name):
        self.open_group_creation()
        self.enter_group_name(name)
        self.create_group()

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_xpath(self.ADD_BUTTON))
        self.click_on_elem(self.ADD_BUTTON)

    def open_group_creation(self):
        self.driver.find_element_by_xpath(self.CREATE_GROUP).click()

    def enter_group_name(self, name):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_xpath(self.GROUP_INPUT))
        self.driver.find_element_by_xpath(self.GROUP_INPUT).send_keys(name)

    def create_group(self):
        self.driver.find_element_by_xpath(self.CREATE_GROUP_BUTTON).click()

    def group_delete(self, name):
        self.hov_elem(self.SIDEBAR_GROUP.format(name))
        self.driver.find_element_by_xpath(self.GROUP_SETTINGS_BUTTON).click()
        self.driver.find_element_by_xpath(self.DELETE_LINK).click()
        self.driver.find_elements_by_xpath(self.CONFIRM_DELETE_BUTTON)[1].click()

    def click_on_elem(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except StaleElementReferenceException:
            self.click_on_elem(xpath)
        except NoSuchElementException:
            self.click_on_elem(xpath)

    def hov_elem(self, xpath):
        try:
            item = WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_xpath(xpath))
            hov = ActionChains(self.driver).move_to_element(item)
            hov.perform()
        except StaleElementReferenceException:
            self.hov_elem(xpath)
        except NoSuchElementException:
            self.hov_elem(xpath)