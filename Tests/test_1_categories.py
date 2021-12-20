from Pages import MainPage
from Pages import SearchResults
from Helpers import helpers

def test_product_search_by_brand(assign_browser, login_to_6pm):
    MainPage.hover_over_accessories_and_select_point(helpers.get_data('test1', 'category'), assign_browser)
    SearchResults.specify_brand(helpers.get_data('test1', 'brand'), assign_browser)
    actual_number_of_items = SearchResults.count_all_found_items(assign_browser)
    print(f'the actual number of found items is {actual_number_of_items}')
    assert actual_number_of_items == int(helpers.wait_for_element(SearchResults.items_found_span, assign_browser).text.split()[0])

