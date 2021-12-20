from Helpers.helpers import *
from selenium.webdriver.common.by import By
from selenium import webdriver

LOCATOR_MY_ACC_BTN = (By.XPATH, '//a[@href="/account"and @class="y-z"]')
LOCATOR_LOGIN_OR_REG_BTN = (By.XPATH, '//div[@class="q-z"]//a[@href="/login"]')
LOCATOR_ACCESSORIES_BTN = (By.XPATH, '//a[@href="/accessories"]')
LOCATOR_SUNGLASSES_BTN = (By.XPATH, '//a[text()="Sunglasses"]')
LOCATOR_BAG_BTN = (By.XPATH, '//a[@href="/cart"]')
LOCATOR_CLOSE_INFO_BUG_POP_UP_BTN = (By.XPATH, '//button[@aria-label="Close"]')
LOCATOR_VIEW_BUG_BTN = (By.XPATH, '//a[@href="/cart" and @class="tt-z"]')
LOCATOR_FAVORITES_BTN = (By.XPATH, '//a[@href="/account/favorites"]')
LOCATOR_WATCHES_BTN = (By.XPATH, '//a[contains(@href, "/watches/")]')
LOCATOR_BAG_COUNT_LABEL = (By.XPATH, '//a[@href="/cart"]/span[1]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver
        self.find_element = find_element
        self.find_elements = find_elements
        self.check_elem_doesnt_present = check_elem_doesnt_present

    def open_url(self, url):
        self.driver.get(url)

    def go_to_login(self):
        find_element(self.driver, LOCATOR_MY_ACC_BTN).click()

    def go_to_sunglasses(self):
        self._hover_to_accessories()
        find_element(self.driver, LOCATOR_SUNGLASSES_BTN).click()

    def go_to_favorites(self):
        find_element(self.driver, LOCATOR_FAVORITES_BTN).click()

    def go_to_watches(self):
        self._hover_to_accessories()
        find_element(self.driver, LOCATOR_WATCHES_BTN).click()

    def _hover_to_accessories(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(find_element(self.driver, LOCATOR_ACCESSORIES_BTN))
        action.perform()

    def get_count_items_in_bug(self, is_empty=False):
        if not is_empty:
            return int(find_element(self.driver, LOCATOR_BAG_COUNT_LABEL).text)
        else:
            return find_element(self.driver, LOCATOR_BAG_COUNT_LABEL).text

    def go_to_bag(self):
        find_element(self.driver, LOCATOR_BAG_BTN).click()
        find_element(self.driver, LOCATOR_VIEW_BUG_BTN).click()
