from tests.base import Component
from selenium.webdriver.support.ui import WebDriverWait


class LetterParams(Component):
    RECEIVER_ADDRESS = "//textarea[@data-original-name='To']"
    SPAN_LEGAL_EMAIL = "//span[@class='js-compose-label compose__labels__label' and @data-text='{0}']"
    SPAN_EMAIL_CONTAINS = "//span[@data-text='{0}']"
    SPAN_INVALID_EMAIL = "//span[@class='js-compose-label compose__labels__label compose__labels__label_invalid']"
    GRAY_BOX = "//div[@class='b-compose__head']"
    REMOVE_ICON = "//span[@class='js-compose-label compose__labels__label' and @data-text='{0}']/i"
    COPY_ADDRESS = "//textarea[@data-original-name='CC']"


    def is_span_right_email(self, email):
        return self.check_exists_by_xpath(self.SPAN_LEGAL_EMAIL.format(email))

    def is_span_wrong_email(self):
        return self.check_exists_by_xpath(self.SPAN_INVALID_EMAIL)

    def set_to_addr(self, address):
        self.driver.find_element_by_xpath(self.RECEIVER_ADDRESS).send_keys(address + " ")

    def unfocus(self):
        self.driver.find_element_by_xpath(self.GRAY_BOX).click()

    def count_emails(self, email):
        return len(self.driver.find_elements_by_xpath(self.SPAN_EMAIL_CONTAINS.format(email)))

    def remove_email(self, email):
        self.driver.find_element_by_xpath(self.REMOVE_ICON.format(email)).click()

    def check_email_removal(self, email):
        return WebDriverWait(self.driver, 10).until_not(lambda s: s.find_element_by_xpath(email))

    def enter_copy_email(self, email):
        self.driver.find_element_by_xpath(self.COPY_ADDRESS).send_keys(email + " ")