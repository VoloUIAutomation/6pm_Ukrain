from Pages.main_page import BasePageHelper
from Pages.product_page import ProductPageHelper
from Pages.bag_page import BagPageHelper


def test_check_bag_label(driver, test_data, config_data):
    page = BasePageHelper(driver)
    page.open_url(test_data['url'])
    page.go_to_sunglasses()
    page = ProductPageHelper(driver)
    for i in range(config_data['count_of_items_in_the_bag']):
        page.add_to_bag(i)
        page.go_to_sunglasses()
    expected_labels_count = page.get_count_items_in_bug()
    assert expected_labels_count == config_data['count_of_items_in_the_bag'], \
        f"Actual count of items = {config_data['count_of_items_in_the_bag']} isn't equal expected count of items = {expected_labels_count}!"
    page.go_to_bag()
    page = BagPageHelper(driver)
    page.remove_all_items_from_bag()
    expected_labels_count = page.get_count_items_in_bug(is_empty=True)
    assert expected_labels_count == 'Cart empty', \
        f"Actual count of items = {config_data['count_of_items_in_the_bag']} isn't equal expected count of items = Cart empty!"
