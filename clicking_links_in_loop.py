import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_log_in(driver):
    driver.get('http://localhost/litecart/admin')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').submit()
    WebDriverWait(driver, 15).until(EC.title_is('My Store'))

    list_of_links = driver.find_elements_by_tag_name('h1')

    for links in enumerate(list_of_links):
        driver.implicitly_wait(4)
        for link in enumerate(links):
            link.click()


