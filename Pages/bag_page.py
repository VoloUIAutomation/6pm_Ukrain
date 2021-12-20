from Pages.base_page import *
from selenium.webdriver.common.by import By
import re
import time

LOCATOR_ITEM_PRICE = (By.XPATH, '//*[@id="main"]/div/div/div/div[1]//em')
LOCATOR_TOTAL_PRICE = (By.XPATH, '//button[text()="Proceed to Checkout"]/following-sibling::dl/dd')
LOCATOR_ITEM = (By.XPATH, '//*[@id="main"]/div/div/div/div/div[@class="Pw-z"]')
LOCATOR_TOTAL_COUNT = (By.XPATH, '//dt[text()="Subtotal"]/span')
LOCATOR_REMOVE_ITEM_BTN = (By.XPATH, '//button[@aria-label="Remove Item"]')
LOCATOR_EMPTY_BAG_MSG = (By.XPATH, '//main//p[contains(text(), "Fill up")]')
LOCATOR_ITEMS_PRICE = (By.XPATH, '//em[@class="Zw-z bx-z" and contains(text(),"$")]')


class BagPageHelper(BasePageHelper):

    def get_total_items(self):
        count = self.find_element(self.driver, LOCATOR_TOTAL_COUNT).text
        return int(re.sub("\\D", "", count))

    def get_total_price(self):
        price = self.find_element(self.driver, LOCATOR_TOTAL_PRICE).text
        return float(re.sub("\\$", "", price))

    def get_items_in_bag(self):
        return self.find_elements(self.driver, LOCATOR_ITEM)

    def remove_all_items_from_bag(self):
        for i in range(len(self.find_elements(self.driver, LOCATOR_REMOVE_ITEM_BTN))):
            self.find_element(self.driver, LOCATOR_REMOVE_ITEM_BTN).click()
            time.sleep(1)

    def get_sum_of_all_item_costs(self):
        elms = self.find_elements(self.driver, LOCATOR_ITEM_PRICE)
        return round(sum([float(re.sub('\\$', '', i.text)) for i in elms]), 2)
