from Helpers import helpers
from selenium.webdriver.common.by import By
from Pages import MainPage
import time


items_count_span = (By.XPATH, '//span[text()=" items"]')
hearts_list_opener = (By.XPATH, '//a[contains(@href, "account/favorites/") and text()="Hearts"]')
unfavorite_item_button = (By.XPATH, '//button[@aria-label="Favorite this item."]')

def get_items_count(driver):
    return helpers.wait_for_element(items_count_span, driver).get_attribute('innerText').split()[0]


def unfavorite_all_items(driver):
    items_in_favorites = int(get_items_count(driver))
    helpers.wait_for_element(hearts_list_opener, driver).click()
    if items_in_favorites > 0:
        print(f'{items_in_favorites} items in favorites')
        favorited_elements = helpers.wait_for_elements(unfavorite_item_button, driver)
        tries_count = 0
        while len(favorited_elements) < items_in_favorites:
            if tries_count == 10:
                raise Exception('Too many retries')
                break
            print(f'Located less element than should be, {len(favorited_elements)} instead of {items_in_favorites}. Will scroll down and wait again')
            tries_count +=1
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            favorited_elements = helpers.wait_for_elements(unfavorite_item_button, driver)
        for k in favorited_elements:
            k.click()
        helpers.wait_for_element(MainPage.favourites_button, driver).click()
        tries_count = 0
        while int(get_items_count(driver)) >0:
            print(f'Actually there is still {get_items_count(driver)} items left in favorites. Will refresh the page and see if it changes')
            if tries_count == 20:
                raise Exception('Too many retries')
                break
            driver.refresh()
            tries_count +=1
            time.sleep(1)
    else:
        print('Favorites list is empty')