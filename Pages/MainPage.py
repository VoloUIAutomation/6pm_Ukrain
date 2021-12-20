from Helpers import helpers
from selenium.webdriver.common.by import By


accessories = (By.XPATH, '//a[@href="/accessories"]')
watches = (By.XPATH, '//*[text()="Oval"]')
sunglasses = (By.XPATH, '//*[text()="Sunglasses"]')
cart_icon = (By.XPATH, '//header//child::a[@href="/cart"]')
favourites_button = (By.XPATH, '//header//child::a[@href="/account/favorites"]')
view_bag_button = (By.XPATH, '//form/a[@href="/cart"]')
bag_items_count = (By.XPATH, '//header//child::a[@href="/cart"]/span[1]')
log_in_icon = (By.XPATH, '//header//child::a[@href="/account"]')

def form_items_locator(items):
    locator = (By.XPATH, f'//*[text()="{items}"]')
    return locator

def hover_over_accessories_and_select_point(button, driver):
    helpers.hover_and_click(accessories, form_items_locator(button), driver)

