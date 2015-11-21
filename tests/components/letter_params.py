from tests.base import Component


class LetterParams(Component):
    RECEIVER_ADDRESS = "//textarea[@data-original-name='To']"
    SPAN_LEGAL_EMAIL = "//span[@class='js-compose-label compose__labels__label']"

    def set_receiver_address(self, address):
        self.driver.find_element_by_xpath(self.RECIEVER_ADDRESS).send_keys(address + " ")

    def is_span_right_email(self):
        return self.check_exists_by_xpath(self.SPAN_LEGAL_EMAIL)