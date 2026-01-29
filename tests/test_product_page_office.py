import pytest
from pages.locators.product_page_office_locators import product_name_loc
from pages.locators.product_page_office_locators import add_product_loc
from pages.locators.product_page_office_locators import quantity_product
from pages.locators.product_page_office_locators import remove_product_loc


@pytest.mark.extended
def test_check_product_name(product_page_office):
    product_page_office.open_page()
    product_name = product_page_office.find(product_name_loc)
    assert product_name.text == "Office Design Software"


def test_add_product(product_page_office):
    product_page_office.open_page()
    button_add = product_page_office.find(add_product_loc)
    button_add.click()
    product_page_office.wait_for_value(quantity_product, "2")


def test_remove_product(product_page_office):
    product_page_office.open_page()
    button_remove = product_page_office.find(remove_product_loc)
    button_remove.click()
    product_page_office.wait_for_value(quantity_product, "1")
