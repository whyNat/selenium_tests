import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox('C:\Program Files (x86)\Mozilla Firefox')
    request.addfinalizer(wd.quit)
    return wd

def test_my_store(driver):
    driver.get('http://localhost/litecart/admin/login.php?redirect_url=%2Flitecart%2Fadmin%2F')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').submit()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))