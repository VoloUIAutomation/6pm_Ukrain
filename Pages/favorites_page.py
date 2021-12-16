from Pages.base_page import *
from selenium.webdriver.common.by import By

LOCATOR_HEARTS_BLOCK = (By.XPATH, '//a[@href="/account/favorites/h."]/div')
LOCATOR_ITEM = (By.XPATH, '//nav[@aria-label="breadcrumb"]/following-sibling::div[2]/div')


class FavoritesPageHelper(BasePageHelper):

    def get_items_count_in_favorites(self):
        self.find_element(self.driver, LOCATOR_HEARTS_BLOCK).click()
        return self.find_elements(self.driver, LOCATOR_ITEM)
