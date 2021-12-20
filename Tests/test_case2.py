from Pages.main_page import BasePageHelper
from Pages.product_page import ProductPageHelper
from Pages.bag_page import BagPageHelper
import time


def test_check_the_add_to_bag_func(driver, test_data, config_data):
    elem = 0
    page = BasePageHelper(driver)
    page.open_url(test_data['url'])
    for i in range(config_data['count_of_items_in_the_bag']):
        page.got_to_sunglasses()
        page = ProductPageHelper(driver)
        page.filter_by_brand(config_data['brand_name'])
        page.add_to_bag(elem)
        page.go_to_bag()
        page = BagPageHelper(driver)
        actual_items_count = len(page.get_items_in_bag())
        expected_items_count = page.get_total_items()
        assert actual_items_count == expected_items_count, \
            f"Actual count of items = {actual_items_count} isn't equal expected count of items = {expected_items_count}!"
        expected_items_total_price = page.get_sum_of_all_item_costs()
        actual_items_total_price = page.get_total_price()
        assert expected_items_total_price == actual_items_total_price, \
            f"Actual total price of items = {expected_items_total_price} isn't equal expected total price of items = {actual_items_total_price}!"
        time.sleep(1)
        elem += 1
