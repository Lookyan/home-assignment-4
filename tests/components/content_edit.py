# coding=UTF-8

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re

from tests.base import Component


# custom expected condition
class text_to_change(object):
    def __init__(self, xpath, text):
        self.locator = (By.XPATH, xpath)
        self.before_text = text

    def __call__(self, driver):
        text = expected_conditions._find_element(driver, self.locator).text
        return text != self.before_text


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
    MORE_ACTIONS_BTN = "//a[contains(@class, 'mce_moreactions')]"
    MINIMIZE_TOOLBAR_BTN = "//a[contains(@class, 'mce_enableTextEditor')]"
    MAXIMIZE_TOOLBAR_BTN = "//a[contains(@class, 'mce_enableHTMLEditor')]"

    TEXT_COLOR_PICK_BTN = "//div[contains(@class, 'mce_forecolor')]//a[@_mce_color='{}']"
    BACK_COLOR_PICK_BTN = "//div[contains(@class, 'mce_backcolor')]//a[@_mce_color='{}']"
    FONT_PICK_BTN = "//div[contains(@class, 'mce_fontactions_menu')]//a[@id='mce_{}_aria']"
    ALIGN_PICK_BTN = "//div[contains(@class, 'Justify{}')]/a"
    INDENT_CHANGE_BTN = "//div[contains(@class, '{}')]/a"
    LIST_INSERT_BTN = "//div[contains(@class, 'Insert{}List')]/a"

    EMOTIONS_TAB_BTN = "//div[contains(@class, 'mceEmotionsTab0')]"
    EMOTION_PICK_BTN = "//img[@class='{}']"
    EMOTION_TEXT_BTN = "//img[contains(@src, '{}')]"

    LINE_INSERT_BTN = "//div[contains(@class, 'InsertHorizontalRule')]/a"
    LINE_THROUGH_BTN = "//div[contains(@class, 'Strikethrough')]/a"
    TRANSLIT_BTN = "//div[contains(@class, 'mceAppTranslit')]/a"
    VIRTUAL_KEYBOARD_BTN = "//div[contains(@class, 'mceAppKeyboard')]/a"
    REMOVE_FORMAT_BTN = "//div[contains(@class, 'RemoveFormat')]/a"

    ADD_LINK_BTN = "//div[contains(@class, 'mceLink')]/a"
    LINK_HREF_FIELD = "//div[contains(@class, 'mceLinkMenu')]//input[@name='href']"
    LINK_TITLE_FIELD = "//div[contains(@class, 'mceLinkMenu')]//input[@name='title']"
    LINK_SUBMIT_BTN = "//div[contains(@class, 'mceLinkMenu')]//input[@type='submit']"

    BIG_TOOLBAR = "//table[contains(@class, 'mceToolbarRow1')]"
    SMALL_TOOLBAR = "//table[contains(@class, 'mceToolbarRow3')]"

    COMPOSE_FRAME_TABLE = "//div[contains(@class, 'composeEditorFrame')]/table[@class='mlruTmpId{}']"
    DESIGN_BTN = "//a[contains(@class, 'mce_design')]"
    DESIGN_PICK_BTN = "//div[contains(@class, 'js-decoration_appearance')]//div[contains(@class, 'compose__decoration__slider__item__inner_big')]"
    DESIGN_CLEAR_BTN = "//div[contains(@class, 'js-decoration_appearance')]//li[contains(@class, 'js-clear')]/div"
    CARDS_BTN = "//a[contains(@class, 'mce_cards')]"
    CARD_PICK_BTN = "//div[contains(@class, 'js-decoration_cards')]//div[contains(@class, 'compose__decoration__slider__item__inner_big')]"
    CARD_CLEAR_BTN = "//div[contains(@class, 'js-decoration_cards')]//li[contains(@class, 'js-clear')]/div"
    CARD_ELEM = BASE + "//img[contains(@src, '/{}.')]"

    SPELLING_CLOSE_BTN = "//div[contains(@class, 'mdl-btn') and div[text()='Закрыть']]"
    SPELLING_NO_ERRORS = "//div[text()='В тексте письма орфографических ошибок не обнаружено.']"
    SAVE_BTN = "//div[contains(@class, 'mdl-btn') and div[text()='Сохранить изменения']]"
    KEYBOARD_KEY_BTN = u"//form[@name='keyb']//input[@value='{}']"

    def switch_to_edit(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.IFRAME)))
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(self.IFRAME))

    def switch_back(self):
        self.driver.switch_to_default_content()

    def _clear_edit(self):
        self.driver.find_element_by_xpath(self.BASE).clear()

    def clear_edit(self):
        self.switch_to_edit()
        self._clear_edit()
        self.switch_back()

    def change_text(self, text):
        self.switch_to_edit()
        self._clear_edit()
        field = self.driver.find_element_by_xpath(self.BASE)
        field.send_keys(text)
        field.click()
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

    def add_simple_style(self, style):
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(getattr(self, style.upper() + '_BTN')).click()

    def check_tag(self, tag):
        self.switch_to_edit()
        elems = len(self.driver.find_elements_by_xpath(self.BASE + '//' + tag))
        self.switch_back()
        return elems

    def check_bold(self):
        return self.check_tag('strong') == 1

    def check_italic(self):
        return self.check_tag('em') == 1

    def check_elem_style(self, style, value, elem='span', child='//'):
        self.switch_to_edit()
        try:
            element = self.driver.find_element_by_xpath(self.BASE + child + elem)
        except NoSuchElementException:
            element = None

        if element is None:
            return False
        css = element.value_of_css_property(style)
        self.switch_back()
        return css == value

    def check_underline(self):
        return self.check_elem_style('text-decoration', 'underline')

    def add_text_color(self, color):
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(self.TEXT_COLOR_BTN).click()
        self.driver.find_element_by_xpath(self.TEXT_COLOR_PICK_BTN.format(color)).click()

    def check_text_color(self, color):
        r, g, b = [int(color[i:i+2], 16) for i in xrange(1, 6, 2)]
        return self.check_elem_style('color', 'rgba({}, {}, {}, 1)'.format(r, g, b))

    def add_background_color(self, color):
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(self.BACK_COLOR_BTN).click()
        self.driver.find_element_by_xpath(self.BACK_COLOR_PICK_BTN.format(color)).click()

    def check_background_color(self, color):
        r, g, b = [int(color[i:i+2], 16) for i in xrange(1, 6, 2)]
        return self.check_elem_style('background-color', 'rgba({}, {}, {}, 1)'.format(r, g, b))

    def pick_font_size(self, size):
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(self.FONT_BTN).click()
        self.driver.find_element_by_xpath(self.FONT_PICK_BTN.format(size - 1)).click()

    def check_font_size(self, size):
        sizes = {1: 10, 2: 12, 3: 15, 4: 18, 5: 24, 6: 36, 7: 42}
        return self.check_elem_style('font-size', '{}px'.format(sizes[size]))

    def pick_font_family(self, fam):
        fonts = {
            'arial': 8,
            'arial black': 9,
            'georgia': 13,
            'comic sans': 11
        }
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(self.FONT_BTN).click()
        self.driver.find_element_by_xpath(self.FONT_PICK_BTN.format(fonts[fam])).click()

    def check_font_family(self, fam):
        fonts = {
            'arial': 'arial,helvetica,sans-serif',
            'arial black': 'arial black,avant garde',
            'georgia': 'georgia,palatino',
            'comic sans': 'comic sans ms,sans-serif'
        }
        return self.check_elem_style('font-family', fonts[fam])

    def add_align(self, align):
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(self.ALIGN_BTN).click()
        self.driver.find_element_by_xpath(self.ALIGN_PICK_BTN.format(align.title())).click()

    def check_align(self, align):
        return self.check_elem_style('text-align', align, 'div')

    def add_indent(self):
        self.driver.find_element_by_xpath(self.INDENT_BTN).click()
        self.driver.find_element_by_xpath(self.INDENT_CHANGE_BTN.format('Indent')).click()

    def remove_indent(self):
        self.driver.find_element_by_xpath(self.INDENT_BTN).click()
        self.driver.find_element_by_xpath(self.INDENT_CHANGE_BTN.format('Outdent')).click()

    def check_indent(self, i):
        # time.sleep(10)
        return self.check_elem_style('margin-left', '{}px'.format(i * 30), '', '')

    def add_text(self, text):
        self.switch_to_edit()
        self.driver.find_element_by_xpath(self.BASE).send_keys(text)
        self.switch_back()

    def add_list(self, order):
        self.driver.find_element_by_xpath(self.LIST_BTN).click()
        self.driver.find_element_by_xpath(self.LIST_INSERT_BTN.format(order.title())).click()

    def check_list(self, order, num=1):
        order_tag = {'ordered': 'ol', 'unordered': 'ul'}
        list_tag = order_tag[order]
        if self.check_tag(list_tag) == 1 and self.check_tag('li') == num:
            return True
        return False

    def add_emotion(self, emotion):
        self.driver.find_element_by_xpath(self.EMOTIONS_BTN).click()
        self.driver.find_element_by_xpath(self.EMOTIONS_TAB_BTN).click()
        self.driver.find_element_by_xpath(self.EMOTION_PICK_BTN.format(emotion)).click()

    def check_emotion(self, emotion):
        self.switch_to_edit()
        found = len(self.driver.find_elements_by_xpath(self.EMOTION_TEXT_BTN.format(emotion)))
        self.switch_back()
        return found >= 1

    def undo(self):
        self.switch_to_edit()
        self.driver.find_element_by_xpath(self.BASE).click()
        self.switch_back()
        self.driver.find_element_by_xpath(self.UNDO_BTN).click()

    def redo(self):
        self.switch_to_edit()
        self.driver.find_element_by_xpath(self.BASE).click()
        self.switch_back()
        self.driver.find_element_by_xpath(self.REDO_BTN).click()

    def add_line(self):
        self.driver.find_element_by_xpath(self.MORE_ACTIONS_BTN).click()
        self.driver.find_element_by_xpath(self.LINE_INSERT_BTN).click()

    def add_link(self, href, title):
        self.driver.find_element_by_xpath(self.MORE_ACTIONS_BTN).click()
        self.driver.find_element_by_xpath(self.ADD_LINK_BTN).click()
        self.driver.find_element_by_xpath(self.LINK_HREF_FIELD).clear()
        self.driver.find_element_by_xpath(self.LINK_HREF_FIELD).send_keys(href)
        self.driver.find_element_by_xpath(self.LINK_TITLE_FIELD).send_keys(title)
        self.driver.find_element_by_xpath(self.LINK_SUBMIT_BTN).click()

    def translit_text(self):
        text = self.get_text()
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(self.MORE_ACTIONS_BTN).click()
        self.driver.find_element_by_xpath(self.TRANSLIT_BTN).click()
        self.switch_to_edit()
        WebDriverWait(self.driver, 5).until(text_to_change(self.BASE, text))
        self.switch_back()

    def remove_format(self):
        self.switch_to_edit()
        self.select_text()
        self.switch_back()
        self.driver.find_element_by_xpath(self.MORE_ACTIONS_BTN).click()
        self.driver.find_element_by_xpath(self.REMOVE_FORMAT_BTN).click()

    def check_line(self):
        return self.check_tag('hr')

    def check_link(self, href, title):
        self.switch_to_edit()
        links = self.driver.find_elements_by_xpath(self.BASE + "/a[@href='{}']".format(href))
        if len(links) != 1:
            return False
        return links[0].text == title

    def check_tags(self):
        return self.check_tag('*')

    def minimize_toolbar(self):
        self.driver.find_element_by_xpath(self.MINIMIZE_TOOLBAR_BTN).click()

    def maximize_toolbar(self):
        self.driver.find_element_by_xpath(self.MAXIMIZE_TOOLBAR_BTN).click()

    def check_toolbar(self):
        return 'big' if self.driver.find_element_by_xpath(self.BIG_TOOLBAR).is_displayed() else 'small'

    def pick_theme(self, num):
        self.driver.find_element_by_xpath(self.DESIGN_BTN).click()
        themes = self.driver.find_elements_by_xpath(self.DESIGN_PICK_BTN)
        themes[num].click()
        self.driver.find_element_by_xpath(self.DESIGN_BTN).click()

    def delete_theme(self):
        self.driver.find_element_by_xpath(self.DESIGN_BTN).click()
        self.driver.find_element_by_xpath(self.DESIGN_CLEAR_BTN).click()
        self.driver.find_element_by_xpath(self.DESIGN_BTN).click()

    def check_theme(self, num):
        themes = self.driver.find_elements_by_xpath(self.DESIGN_PICK_BTN)
        url = themes[num].value_of_css_property('background-image')
        internal_num = re.search('([0-9]+)\.[a-z]+\"\)$', url).group(1)
        elems = self.driver.find_elements_by_xpath(self.COMPOSE_FRAME_TABLE.format(internal_num))
        return len(elems) > 0

    def pick_card(self, num):
        self.driver.find_element_by_xpath(self.CARDS_BTN).click()
        cards = self.driver.find_elements_by_xpath(self.CARD_PICK_BTN)
        cards[num].click()
        self.driver.find_element_by_xpath(self.CARDS_BTN).click()

    def delete_card(self):
        self.driver.find_element_by_xpath(self.CARDS_BTN).click()
        self.driver.find_element_by_xpath(self.CARD_CLEAR_BTN).click()
        self.driver.find_element_by_xpath(self.CARDS_BTN).click()

    def check_card(self, num):
        cards = self.driver.find_elements_by_xpath(self.CARD_PICK_BTN)
        url = cards[num].value_of_css_property('background-image')
        internal_num = re.search('([0-9]+)i\.[a-z]+\"\)$', url).group(1)
        self.switch_to_edit()
        elems = self.driver.find_elements_by_xpath(self.CARD_ELEM.format(internal_num))
        self.switch_back()
        return len(elems) > 0

    def check_spelling(self):
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = self.driver.current_window_handle
        self.driver.find_element_by_xpath(self.SPELLING_BTN).click()
        spelling_window_handle = None
        while not spelling_window_handle:
            for handle in self.driver.window_handles:
                if handle != main_window_handle:
                    spelling_window_handle = handle
                    break
        self.driver.switch_to.window(spelling_window_handle)
        text = self.driver.find_elements_by_xpath(self.SPELLING_NO_ERRORS)
        self.driver.find_element_by_xpath(self.SPELLING_CLOSE_BTN).click()
        self.driver.switch_to.window(main_window_handle)
        return len(text) == 1

    def translate(self):
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = self.driver.current_window_handle
        self.driver.find_element_by_xpath(self.TRANSLATE_BTN).click()
        spelling_window_handle = None
        while not spelling_window_handle:
            for handle in self.driver.window_handles:
                if handle != main_window_handle:
                    spelling_window_handle = handle
                    break
        self.driver.switch_to.window(spelling_window_handle)
        self.driver.find_element_by_xpath(self.SAVE_BTN).click()
        self.driver.switch_to.window(main_window_handle)

    def virtual_keyboard_type(self, text):
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = self.driver.current_window_handle
        self.driver.find_element_by_xpath(self.MORE_ACTIONS_BTN).click()
        self.driver.find_element_by_xpath(self.VIRTUAL_KEYBOARD_BTN).click()
        spelling_window_handle = None
        while not spelling_window_handle:
            for handle in self.driver.window_handles:
                if handle != main_window_handle:
                    spelling_window_handle = handle
                    break
        self.driver.switch_to.window(spelling_window_handle)
        for ch in text:
            self.driver.find_element_by_xpath(self.KEYBOARD_KEY_BTN.format(ch)).click()
        self.driver.find_element_by_xpath(self.SAVE_BTN).click()
        self.driver.switch_to.window(main_window_handle)