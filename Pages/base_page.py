from Helpers.helpers import *

LOCATOR_MY_ACC_BTN = ()
LOCATOR_LOGIN_OR_REG_BTN = ()
LOCATOR_ACCESSORIES_BTN = ()
LOCATOR_SUNGLASSES_BTN = ()
LOCATOR_BAG_BTN = ()
LOCATOR_CLOSE_INFO_BUG_POP_UP_BTN = ()
LOCATOR_VIEW_BUG_BTN = ()
LOCATOR_FAVORITES_BTN = ()
LOCATOR_WATCHES_BTN = ()
LOCATOR_BAG_COUNT_LABEL = ()


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver
        self.find_element = find_element
        self.find_elements = find_elements
        self.check_elem_doesnt_present = check_elem_doesnt_present

    def go_to_login(self):
        find_element(self.driver, LOCATOR_MY_ACC_BTN).click()
        find_element(self.driver, LOCATOR_LOGIN_OR_REG_BTN).click()

    def got_to_sunglasses(self):
        find_element(self.driver, LOCATOR_ACCESSORIES_BTN).click()
        find_element(self.driver, LOCATOR_SUNGLASSES_BTN).click()

    def go_to_favorites(self):
        find_element(self.driver, LOCATOR_ACCESSORIES_BTN).click()
        find_element(self.driver, LOCATOR_WATCHES_BTN).click()

    def go_to_watches(self):
        find_element(self.driver, LOCATOR_ACCESSORIES_BTN).click()
        find_element(self.driver, LOCATOR_WATCHES_BTN).click()

    def get_count_items_in_bug(self, is_empty=False):
        if not is_empty:
            return find_element(self.driver, LOCATOR_BAG_COUNT_LABEL).text
        else:
            return check_elem_doesnt_present(self.driver, LOCATOR_BAG_COUNT_LABEL)
