import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_checking_if_sorted_countries(driver):
    driver.get('http://localhost/litecart/admin')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').submit()


    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="box-apps-menu-wrapper"]//li[3]/a/span[@class="name"]').click()

    sort_element = driver.find_elements_by_xpath('//*[@id="main"]//td[5]/a')
    country_names = []

    for i in sort_element:
        names = i.get_attribute('textContent')
        country_names.append(names)

    print(country_names)
    sorted_country_names = sorted(country_names)

    i = 0
    countriesSorted = True
    for k in sorted_country_names:
        if k != country_names[i]:
            print('SORTED NAME: ' + k + ', ORIGINAL NAME: ' + country_names[i])
            countriesSorted = False
        i += 1

    if not countriesSorted:
        print('Nieposortowane DO JASNEJ CHOLERY!')












#driver.assertEquals(sort_element, "IPhone")

#sort_element =