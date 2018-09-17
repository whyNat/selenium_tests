import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_right_side_of_product(driver):
    driver.get('http://localhost/litecart/en/')
    driver.find_element_by_css_selector('ul.nav li.category-1 a').click()

    all_products = driver.find_elements_by_css_selector('.product')

    for product in all_products:
        check_name = product.get_attribute('name')
        check_product = product.click()
        open_product_name = driver.find_element_by_css_selector('h1.class')
        check_open_product_name = open_product_name.get_attribute('title')
        assert check_name == check_open_product_name
