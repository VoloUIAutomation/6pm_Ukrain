from Pages.main_page import BasePageHelper
from Pages.product_page import ProductPageHelper


def test_check_the_product_search_by_brand(driver, test_data, config_data):
    page = BasePageHelper(driver)
    page.open_url(test_data['url'])
    page.go_to_sunglasses()
    page = ProductPageHelper(driver)
    page.filter_by_brand(config_data['brand_name'])
    expected_items_count = page.get_filter_count(config_data['brand_name'])
    actual_items_count = len(page.get_product_items())
    assert expected_items_count == actual_items_count, \
        f"Actual count of items = {expected_items_count} isn't equal expected count of items = {actual_items_count}!"
