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

    list_of_products = driver.find_elements_by_xpath('//*[class="col-xs-6 col-sm-4 col-md-3"]')

    for i in list_of_products:
        number = driver.find_elements_by_xpath('//*[@class="sticker sale"]')
        number2 = driver.find_elements_by_xpath('//*[@class="sticker new"]')
        total = len(number) + len(number2)
        if i in number or i in number2:
            assert total == len(list_of_products)
        else:
            print('There\'s more than 1 sticker on product')





