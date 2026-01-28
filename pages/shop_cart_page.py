from pages.base_page import BasePage
from pages.locators.shop_cart_locators import title_shop_cart_locator


class ShopCartPage(BasePage):
    page_url = "shop/cart"


    def check_title(self, text):
        self.find(title_shop_cart_locator)
        assert title_shop_cart_locator.text == text
        