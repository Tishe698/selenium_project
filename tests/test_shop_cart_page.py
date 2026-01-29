import pytest
from pages.locators.shop_cart_locators import header_shop_cart_loc
from pages.locators.shop_cart_locators import basket_empty_text_loc


@pytest.mark.extended
def test_title(shop_cart_page):
    shop_cart_page.open_page()
    shop_cart_page.check_title("Shopping Cart | My Website")


@pytest.mark.extended
def test_header_shop_cart(shop_cart_page):
    shop_cart_page.open_page()
    header_shop_cart = shop_cart_page.find(header_shop_cart_loc)
    assert header_shop_cart.text == "Order overview"


@pytest.mark.extended
def test_basket_text(shop_cart_page):
    shop_cart_page.open_page()
    basket_empty_text = shop_cart_page.find(basket_empty_text_loc)
    assert basket_empty_text.text == "Your cart is empty!"
