
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_registration(driver):
    driver.get('http://localhost/litecart/en/')
    sign_in_elem = driver.find_element_by_xpath('//*[@id ="default-menu"]//a')
    sign_in_elem.send_keys(Keys.TAB)
    sign_in_elem.click()
    time.sleep(1)
    new_customer_elem = driver.find_element_by_xpath('//*[@id ="default-menu"]/ul[2]/li/ul//a')
    driver.execute_script("arguments[0].click()", new_customer_elem)

    driver.find_element_by_xpath('//*[@id="box-create-account"]//div[1]/input').send_keys('Andrew')
    driver.find_element_by_xpath('//*[@id="box-create-account"]//div[2]/input').send_keys('Dudek')
    driver.find_element_by_xpath('//*[@id="box-create-account"]//select').click()
    country_elem = driver.find_element_by_xpath('//*[@id="box-create-account"]//option[value="VG"]')
    driver.execute_script("arguments[0].click()", country_elem)


