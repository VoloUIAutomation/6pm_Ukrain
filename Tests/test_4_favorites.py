from Pages import MainPage
from Pages import SearchResults
from Pages import Favorites
from Helpers import helpers

def test_favorites_count(assign_browser, login_to_6pm, unfavorite_all_favorited_items):
    MainPage.hover_over_accessories_and_select_point(helpers.get_data('test4', 'category'), assign_browser)
    items_number = helpers.get_data('test4', 'number')
    SearchResults.favourite_n_items(items_number, assign_browser)
    helpers.wait_for_element(MainPage.favourites_button, assign_browser).click()
    the_count_shown_in_favourites = Favorites.get_items_count(assign_browser)
    print(the_count_shown_in_favourites)
    assert int(the_count_shown_in_favourites) == items_number


