from Pages.base_page import BasePageHelper

LOCATOR_ADD_TO_FAVORITES_BTN = ()
LOCATOR_SEARCH_BRAND_INPUT = ()
LOCATOR_BRAND_CHECKBOX = ()


class SunglassesPageHelper(BasePageHelper):

    def filter_by_brand(self, brand_name):
        self.find_element(self.driver, LOCATOR_SEARCH_BRAND_INPUT).send_keys(brand_name)
        self.find_element(self.driver, LOCATOR_BRAND_CHECKBOX).click()
        return self

