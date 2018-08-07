import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#create capabilities
capabilities = DesiredCapabilities.INTERNETEXPLORER

#delete platform and version keys
capabilities.pop("platform", None)
capabilities.pop("version", None)

@pytest.fixture
def driver(request):
    wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd

def test_my_store(driver):
    driver.get('http://localhost/litecart/admin/login.php?redirect_url=%2Flitecart%2Fadmin%2F')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').submit()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))