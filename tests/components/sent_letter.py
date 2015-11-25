# coding=UTF-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from tests.base import Component


class SentLetter(Component):

    SENT_LETTER_INFO = "//div[contains(@class, 'message-sent') and a]"

    def check_sent_letter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, self.SENT_LETTER_INFO)))
        return u'письмо отправлено' in self.driver.find_element_by_xpath(self.SENT_LETTER_INFO).text
