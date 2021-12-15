from Pages.base_page import *

LOCATOR_ADD_TO_FAVORITES_BTN = ()
LOCATOR_SEARCH_BRAND_INPUT = ()
LOCATOR_BRAND_CHECKBOX = ()
LOCATOR_PRODUCT_ITEM = ()


class ProductPageHelper(BasePageHelper):

    def filter_by_brand(self, brand_name):
        self.find_element(self.driver, LOCATOR_SEARCH_BRAND_INPUT).send_keys(brand_name)
        self.find_element(self.driver, LOCATOR_BRAND_CHECKBOX).click()

    def get_product_items(self):
        return self.find_elements(self.driver, LOCATOR_PRODUCT_ITEM)

    def get_filter_count(self):
        return self.find_element(self.driver, LOCATOR_BRAND_CHECKBOX).text

    def add_to_favorites(self):
        self.find_element(self.driver, LOCATOR_ADD_TO_FAVORITES_BTN).click()

