from Helpers.helpers import *

LOCATOR_MY_ACC_BTN = ()
LOCATOR_LOGIN_OR_REG_BTN = ()
LOCATOR_ACCESSORIES_BTN = ()
LOCATOR_SUNGLASSES_BTN = ()


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver
        self.find_element = find_element
        self.find_elements = find_elements

    def go_to_login(self):
        find_element(self.driver, LOCATOR_MY_ACC_BTN).click()
        find_element(self.driver, LOCATOR_LOGIN_OR_REG_BTN).click()
        return self

    def got_to_sunglasses(self):
        find_element(self.driver, LOCATOR_ACCESSORIES_BTN).click()
        find_element(self.driver, LOCATOR_SUNGLASSES_BTN).click()
        return self
