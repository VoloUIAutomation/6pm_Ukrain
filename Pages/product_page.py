from Pages.base_page import *
from selenium.webdriver.common.by import By
import re

LOCATOR_ADD_TO_FAVORITES_BTN = (By.XPATH, '//button[@data-test-id="heartButton"]')
LOCATOR_SEARCH_BRAND_INPUT = (By.ID, 'Brand')
LOCATOR_BRAND_CHECKBOX = (By.XPATH, '//ul[@aria-labelledby="brandNameFacet"]/li//span[2]')
LOCATOR_PRODUCT_ITEM = (By.XPATH, '//div[@id="products"]/article')


class ProductPageHelper(BasePageHelper):

    def filter_by_brand(self, brand_name):
        self.find_element(self.driver, LOCATOR_SEARCH_BRAND_INPUT).send_keys(brand_name)
        self.find_element(self.driver, LOCATOR_BRAND_CHECKBOX).click()

    def get_product_items(self):
        return self.find_elements(self.driver, LOCATOR_PRODUCT_ITEM)

    def get_filter_count(self):
        count = self.find_element(self.driver, LOCATOR_BRAND_CHECKBOX).get_attribute("aria-label")
        return int(re.sub("\\D", "", count))

    def add_to_favorites(self):
        self.find_element(self.driver, LOCATOR_ADD_TO_FAVORITES_BTN).click()
