import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_sticker_products(driver):
    driver.get('http://localhost/litecart/en/')
    driver.find_element_by_css_selector('#box-category-tree a').click()

    list_of_products = driver.find_elements_by_css_selector('.product')
    count_products = len(list_of_products)
    number = driver.find_elements_by_css_selector('.sticker')
    count_stickers = len(number)


    if count_products == count_stickers:
        print('There\'s only 1 sticker on product')
    else:
        print('There\'s different number of stickers and products')











