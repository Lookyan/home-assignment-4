from tests.base import Component


class ContentEdit(Component):
    IFRAME = "//div[@class='composeEditorFrame']//iframe"
    BASE = "//body[@id='tinymce']"

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