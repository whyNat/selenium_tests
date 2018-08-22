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
    driver.find_element_by_xpath('//*[@id="box-category-tree"]/ul/li/a').click()

    list_of_products = driver.find_elements_by_class_name('image img-responsive')
    count_products = len(list_of_products)
    number = driver.find_elements_by_xpath('//*[@id="box-category"]/img[contains(@class, "sticker")')
    count_stickers = len(number)

    for i in list_of_products:
        if count_products == count_stickers:
            print('There\'s only than 1 sticker on product')
        else:
            print('There\'s more than 1 sticker on product')









