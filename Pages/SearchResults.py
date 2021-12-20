from Helpers import helpers
from selenium.webdriver.common.by import By
import time

item = (By.XPATH, '//div[@id="products"]/article')
next_page_button = (By.XPATH, '//a[text()="Next"]')
items_found_span = (By.XPATH, '//span[contains(text(), "items found")]')
brand_search_field = (By.XPATH, '//input[@type="text" and @id="Brand"]')
favourite_this_item = (By.XPATH, '//button[@aria-label="Favorite this item."]')

def form_brand_checkbox_locator(brand):
    locator = (By.XPATH, f'//a/span[text()="{brand}"]')
    return locator

def specify_brand(brand, driver):
    the_field = helpers.wait_for_element(brand_search_field, driver)
    the_field.clear()
    the_field.send_keys(brand)
    helpers.wait_for_element(form_brand_checkbox_locator(brand), driver).click()


def count_all_found_items(driver):
    the_count = 0
    while True:
        the_count += len(helpers.wait_for_elements(item, driver))
        if len(driver.find_elements(*next_page_button)) == 0:
            break
        the_button = helpers.wait_for_element(next_page_button, driver)
        if not the_button.is_displayed():
            print('the button is disabled')
            break
        the_button.click()
    return the_count

def favourite_n_items(number, driver):
    for k in helpers.wait_for_elements(favourite_this_item, driver)[:number]:
        print('favorited an item')
        k.click()
    time.sleep(3)


