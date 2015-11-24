# coding=UTF-8

from tests.base import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.errorhandler import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.expected_conditions import invisibility_of_element_located


class LetterParams(Component):
    RECEIVER_ADDRESS = "//textarea[@data-original-name='To']"
    SPAN_LEGAL_EMAIL = "//span[@class='js-compose-label compose__labels__label' and contains(@data-text,'{0}')]"
    SPAN_EMAIL_CONTAINS = "//span[@data-text='{0}']"
    SPAN_INVALID_EMAIL = "//span[@class='js-compose-label compose__labels__label compose__labels__label_invalid']"
    GRAY_BOX = "//div[@class='b-compose__head']"
    REMOVE_ICON = "//span[@class='js-compose-label compose__labels__label' and @data-text='{0}']/i"
    COPY_ADDRESS = "//textarea[@data-original-name='CC']"
    TOPIC = "//input[@name='Subject']"
    TOPIC_BUTTON = "//label[contains(., 'Тема') and @class='compose__header__label js-label']"
    CONTACT_DROPDOWN = "//div[@data-original-name='{0}']/div/div[contains(@class, 'js-dropdown-item') and contains(@data-suggest, '{1}')]"
    REMOVE_ICON_ANY = "//span[@class='js-compose-label compose__labels__label' and contains(@data-text, '{0}')]/i"
    ADDRESSBOOK_CHOOSE_BUTTON = "//div[@title='Адресная книга' and @data-type='{0}']"

    PICK_BY_EMAIL = "//div[contains(., '{0}')]/label/input[@title='Выбрать']"
    PICK_ALL = "//div[@data-name='mainCheck']/div"
    SELECTED_ITEM = "//div[contains(@class, 'messageline_selected')]"
    ADD_CONTACT = "//div[@data-name='add']/span[contains(.,'Добавить')]"


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

    def enter_topic(self, text):
        self.driver.find_element_by_xpath(self.TOPIC).send_keys(text)

    def check_topic_text(self, text):
        return self.driver.find_element_by_xpath(self.TOPIC).get_attribute("value") == text

    def click_topic_for_focus(self):
        self.driver.find_element_by_xpath(self.TOPIC_BUTTON).click()

    def check_focus_on_topic_input(self):
        return self.driver.find_element_by_xpath(self.TOPIC) == self.driver.switch_to_active_element()

    def focus_on(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def choose_contact(self, email, field):
        # self.unfocus()
        if field == 'To':
            self.click_on_elem(self.RECEIVER_ADDRESS)
        elif field == 'CC':
            self.driver.find_element_by_xpath(self.COPY_ADDRESS).click()
        dropdown = WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_xpath(self.CONTACT_DROPDOWN.format(field, email)))
        dropdown.click()

    def remove_email_any(self, sub):
        self.driver.find_element_by_xpath(self.REMOVE_ICON_ANY.format(sub)).click()
        # WebDriverWait(self.driver, 10).until(invisibility_of_element_located())

    def leave_confirm_off(self):
        self.driver.execute_script("window.onbeforeunload = null;")

    def click_address_book(self, type):
        self.driver.find_element_by_xpath(self.ADDRESSBOOK_CHOOSE_BUTTON.format(type)).click()
        window = self.driver.window_handles[1]
        self.driver.switch_to_window(window)

    def pick_by_email(self, email):
        self.driver.find_element_by_xpath(self.PICK_BY_EMAIL.format(email)).click()

    def pick_all_emails(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_xpath(self.PICK_ALL))
        self.driver.find_element_by_xpath(self.PICK_ALL).click()

    def is_email_selected(self):
        return self.check_exists_by_xpath(self.SELECTED_ITEM)

    def click_add_contact(self):
        self.driver.find_element_by_xpath(self.ADD_CONTACT).click()

    def switch_to_main_window(self):
        window = self.driver.window_handles[0]
        self.driver.switch_to_window(window)

    def click_on_elem(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except StaleElementReferenceException:
            self.click_on_elem(xpath)
        except NoSuchElementException:
            self.click_on_elem(xpath)