from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from Helpers import helpers
from Pages import LogInForm, MainPage, Favorites
import time


@pytest.fixture(scope='session', autouse=True)
def assign_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=False)
def login_to_6pm(assign_browser):
    helpers.page_load(helpers.get_config('the_url'), assign_browser)
    helpers.wait_for_element(MainPage.log_in_icon, assign_browser).click()
    LogInForm.sign_in(helpers.get_config('user1', 'login'), helpers.get_config('user1', 'password'), assign_browser)
    time.sleep(5)


@pytest.fixture(scope='function', autouse=False)
def unfavorite_all_favorited_items(assign_browser):
    print('Executing unfavorite items')
    helpers.wait_for_element(MainPage.favourites_button, assign_browser).click()
    Favorites.unfavorite_all_items(assign_browser)


@pytest.fixture(scope='function', autouse=False)
def clear_cookies(assign_browser):
    assign_browser.delete_all_cookies()