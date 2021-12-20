from Pages.main_page import BasePageHelper
from Pages.product_page import ProductPageHelper
from Pages.login_page import LoginPageHelper
from Pages.favorites_page import FavoritesPageHelper


def test_check_favorites(driver, test_data, config_data):
    page = BasePageHelper(driver)
    page.open_url(test_data['url'])
    page.go_to_login()
    page = LoginPageHelper(driver)
    page.login(test_data['user_account']['email'], test_data['user_account']['psw'])
    page.go_to_watches()
    page = ProductPageHelper(driver)
    for i in range(config_data['count_of_items_in_favorites']):
        page.add_to_favorites(i)
    page.go_to_favorites()
    page = FavoritesPageHelper(driver)
    items_in_favorites = page.get_items_count_in_favorites()
    assert len(items_in_favorites) == config_data['count_of_items_in_favorites'], \
        f"Actual count of items = {len(items_in_favorites)} isn't equal expected count of items = {config_data['count_of_items_in_favorites']}!"
