# coding=UTF-8

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.base import Component


# custom expected condition
class successful_save_template(object):
    def __init__(self, save_more_btn_xpath, save_template_btn_xpath, save_status_xpath, save_status_text):
        self.save_more_xp = save_more_btn_xpath
        self.save_template_xp = save_template_btn_xpath
        self.save_status_xp = save_status_xpath
        self.save_status_txt = save_status_text

    def __call__(self, driver):
        try:
            more_btn = driver.find_element_by_xpath(self.save_more_xp)
        except NoSuchElementException:
            return False
        more_btn.click()
        try:
            save_template_btn = driver.find_element_by_xpath(self.save_template_xp)
        except NoSuchElementException:
            more_btn.click()
            return False
        save_template_btn.click()
        # more_btn.click()
        try:
            WebDriverWait(driver, 3).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, self.save_status_xp), self.save_status_txt)
            )
        except TimeoutException:
            return False
        return True


class MainToolbar(Component):

    CANCEL_BTN = "//div[@data-name='cancel']"

    SAVE_MORE_BTN = "//div[@data-group='save-more']/div[@data-mnemo]/.."
    SAVE_TEMPLATE_BTN = "//div[@data-group='save-more']//a[@data-name='saveTemplate' and not(contains(@class, 'b-dropdown__list__item_disabled'))]"
    SAVE_STATUS = "//div[@data-mnemo='saveStatus']"

    TEMPLATES_BTN = "//div[@data-group='templates']/div[@data-mnemo]"
    TEMPLATE_PICK_BTN = "//div[@data-group='templates']//a[contains(@data-text, '{}')]"

    def save_template(self):
        WebDriverWait(self.driver, 5).until(successful_save_template(self.SAVE_MORE_BTN, self.SAVE_TEMPLATE_BTN,
                                                                     self.SAVE_STATUS, u'Сохранено в'))

    def check_template(self, template):
        self.driver.find_element_by_xpath(self.TEMPLATES_BTN).click()
        try:
            WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, self.TEMPLATE_PICK_BTN.format(template))))
            return True
        except TimeoutException:
            return False

    def use_template(self, template):
        self.driver.find_element_by_xpath(self.TEMPLATES_BTN).click()
        self.driver.find_element_by_xpath(self.TEMPLATE_PICK_BTN.format(template)).click()

    def cancel(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located((By.XPATH, self.CANCEL_BTN)))
        self.driver.find_element_by_xpath(self.CANCEL_BTN).click()
        try:
            WebDriverWait(self.driver, 3).until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to_alert()
            alert.accept()
        except TimeoutException:
            pass
