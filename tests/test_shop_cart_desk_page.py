import pytest
from pages.locators.desk_page_locators import button_basket_loc
from pages.locators.desk_page_locators import modal_header_loc
from pages.locators.desk_page_locators import product_img_two_loc
from pages.locators.desk_page_locators import search_input_loc


@pytest.mark.extended
def test_click_on_basket(shop_cart_page_desk):
    shop_cart_page_desk.open_page()
    basket_icon = shop_cart_page_desk.hover(button_basket_loc)
    basket_icon.click()
    modal_add_to_cart = shop_cart_page_desk.wait_for_element(modal_header_loc)
    assert modal_add_to_cart.text == "Add to cart"


@pytest.mark.extended
def test_find_two_img(shop_cart_page_desk):
    shop_cart_page_desk.open_page()
    two_desk = shop_cart_page_desk.find(product_img_two_loc)
    assert two_desk.is_displayed()


@pytest.mark.extended
def test_write_to_search_input(shop_cart_page_desk):
    shop_cart_page_desk.open_page()
    input_search = shop_cart_page_desk.wait_for_element(search_input_loc)
    input_search.click()
    input_search.send_keys("test_text")
