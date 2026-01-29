from selenium import webdriver
import pytest
from pages.shop_cart_page import ShopCartPage
from pages.shop_cart_desk_page import ShopCartPageDesk
from pages.product_page_office import ProductPageOffice


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def shop_cart_page(driver):
    return ShopCartPage(driver)


@pytest.fixture
def shop_cart_page_desk(driver):
    return ShopCartPageDesk(driver)


@pytest.fixture
def product_page_office(driver):
    return ProductPageOffice(driver)
