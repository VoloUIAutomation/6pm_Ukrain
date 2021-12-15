from Pages.base_page import *

LOCATOR_ITEM_PRICE = ()
LOCATOR_TOTAL_PRICE = ()
LOCATOR_ITEM = ()
LOCATOR_TOTAL_COUNT = ()
LOCATOR_REMOVE_ITEM_BTN = ()
LOCATOR_EMPTY_BAG_MSG = ()


class BagPageHelper(BasePageHelper):

    def get_total_items(self):
        return self.find_element(self.driver, LOCATOR_TOTAL_COUNT).text

    def get_total_price(self):
        return self.find_element(self.driver, LOCATOR_TOTAL_PRICE).text

    def get_items_in_bag(self):
        return self.find_elements(self.driver, LOCATOR_ITEM)