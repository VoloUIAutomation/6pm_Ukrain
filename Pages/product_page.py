from Pages.base_page import *
from selenium.webdriver.common.by import By
import re

LOCATOR_ADD_TO_FAVORITES_BTN = (By.XPATH, '//button[@data-test-id="heartButton"]')
LOCATOR_SEARCH_BRAND_INPUT = (By.ID, 'Brand')
LOCATOR_BRAND_CHECKBOX = (By.XPATH, '//ul[@aria-labelledby="brandNameFacet"]/li//span[2]')
LOCATOR_BRAND_CHECKBOX_COUNTER = (
    By.XPATH, '//ul[@aria-labelledby="brandNameFacet"]//span[text()="{}"]/following-sibling::span')
LOCATOR_PRODUCT_ITEM = (By.XPATH, '//div[@id="products"]/article')
LOCATOR_ADD_TO_BAG_BTN = (By.XPATH, '//*[@id="sizingChooser"]/following-sibling::div//button[@type="submit"]')


class ProductPageHelper(BasePageHelper):

    def filter_by_brand(self, brand_name):
        self.find_element(self.driver, LOCATOR_SEARCH_BRAND_INPUT).send_keys(brand_name)
        self.find_element(self.driver, LOCATOR_BRAND_CHECKBOX).click()

    def get_product_items(self):
        return self.find_elements(self.driver, LOCATOR_PRODUCT_ITEM)

    def get_filter_count(self, brand_name):
        elem = LOCATOR_BRAND_CHECKBOX_COUNTER[0], LOCATOR_BRAND_CHECKBOX_COUNTER[1].format(brand_name)
        count = self.find_element(self.driver, elem).get_attribute("aria-label")
        return int(re.sub("\\D", "", count))

    def add_to_favorites(self):
        self.find_element(self.driver, LOCATOR_ADD_TO_FAVORITES_BTN).click()

    def add_to_bag(self, position_of_item):
        items = self.find_elements(self.driver, LOCATOR_PRODUCT_ITEM)
        items[position_of_item].click()
        self.find_element(self.driver, LOCATOR_ADD_TO_BAG_BTN).click()
        self.find_element(self.driver, LOCATOR_CLOSE_INFO_BUG_POP_UP_BTN).click()
