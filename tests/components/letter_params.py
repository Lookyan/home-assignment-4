from tests.base import Component


class LetterParams(Component):
    RECEIVER_ADDRESS = "//textarea[@data-original-name='To']"
    SPAN_LEGAL_EMAIL = "//span[@class='js-compose-label compose__labels__label']"

    def set_receiver_address(self, address):
        self.driver.find_element_by_xpath(self.RECEIVER_ADDRESS).send_keys(address + " ")

    def is_span_right_email(self, address):
        return self.driver.find_element_by_xpath(self.SPAN_LEGAL_EMAIL).text
        # return WebDriverWait(self.driver, 30, 0.1).until(
        #     lambda d: d.find_element_by_xpath(self.SPAN_LEGAL_EMAIL).text
        # )