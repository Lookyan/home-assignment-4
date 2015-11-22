import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from tests.base import Component


class ContentEdit(Component):
    IFRAME = "//div[@class='composeEditorFrame']//iframe"
    BASE = "//body[@id='tinymce']"
    BASE_BTN = "//span[contains(@class, 'mce_{}')]"
    BOLD_BTN = BASE_BTN.format('bold')
    ITALIC_BTN = BASE_BTN.format('italic')
    UNDERLINE_BTN = BASE_BTN.format('underline')
    TEXT_COLOR_BTN = BASE_BTN.format('forecolor')
    BACK_COLOR_BTN = BASE_BTN.format('backcolor')
    FONT_BTN = BASE_BTN.format('fontactions')
    ALIGN_BTN = BASE_BTN.format('justifyselect')
    INDENT_BTN = BASE_BTN.format('textindentactions')
    LIST_BTN = BASE_BTN.format('bullistactions')
    EMOTIONS_BTN = BASE_BTN.format('emotions')
    UNDO_BTN = BASE_BTN.format('undo')
    REDO_BTN = BASE_BTN.format('redo')
    SPELLING_BTN = BASE_BTN.format('appspelling')
    TRANSLATE_BTN = BASE_BTN.format('apptransfer')

    def switch_to_edit(self):
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(self.IFRAME))

    def switch_back(self):
        self.driver.switch_to_default_content()

    def clear_edit(self):
        self.driver.find_element_by_xpath(self.BASE).clear()

    def change_text(self, text):
        self.switch_to_edit()
        self.clear_edit()
        self.driver.find_element_by_xpath(self.BASE).send_keys(text)
        self.switch_back()

    def get_text(self):
        self.switch_to_edit()
        text = self.driver.find_element_by_xpath(self.BASE).text
        self.switch_back()
        return text

    def send_backspaces(self, num):
        self.switch_to_edit()
        for _ in xrange(num):
            self.driver.find_element_by_xpath(self.BASE).send_keys('\b')
        self.switch_back()

    def select_text(self):
        area = self.driver.find_element_by_xpath(self.BASE)
        ActionChains(self.driver).move_to_element_with_offset(area, 10, 10).double_click().perform()

    def add_style(self, style):
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(getattr(self, style.upper() + '_BTN')).click()

    def check_tag(self, tag):
        self.switch_to_edit()
        try:
            self.driver.find_element_by_xpath(self.BASE + '//' + tag)
            ret = True
        except NoSuchElementException:
            ret = False
        finally:
            self.switch_back()
        return ret

    def check_bold(self):
        return self.check_tag('strong')