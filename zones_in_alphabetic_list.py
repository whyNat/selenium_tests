import pytest
from selenium import webdriver
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
    driver.find_element_by_css_selector('.table a:not([title=Edit])').click()

    sort_element = driver.find_elements_by_xpath('//*[@id="main"]//td[5]/a')
    country_names = []

    for i in sort_element:
        names = i.get_attribute('textContent')
        country_names.append(names)

    sorted_country_names = sorted(country_names)

    i = 0
    countries_sorted = True
    for k in sorted_country_names:
        if k != country_names[i]:
            print('SORTED NAME: ' + k + ', ORIGINAL NAME: ' + country_names[i])
            countries_sorted = False
        i += 1

    if not countries_sorted:
        print('Unsorted, DAMN IT!')


def test_checking_if_sorted_in_zones(driver):
    driver.get('http://localhost/litecart/admin')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').submit()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="box-apps-menu-wrapper"]//li[3]/a/span[@class="name"]').click()
    home = driver.current_url

    # nr_zones = driver.find_elements_by_xpath('//*[@id="main"]//td[6][@class="text-center"]')
    # nr_countries = driver.find_elements_by_xpath('//*[@id ="main"]//td[5]/a')





    still_finding_zones = True
    index = 0

    while (still_finding_zones):
        countries_zone_nr = driver.find_elements_by_xpath(
            '//*[@id="main"]//td[6][@class="text-center"]')  # driver.elements.getXPath...
        countries = driver.find_elements_by_xpath('//*[@id ="main"]//td[5]/a')  # driver.elements.getXPath...

        zones_exist = False

        while index < len(countries_zone_nr):
            zones_exist = False

            number = countries_zone_nr[index].get_attribute('textContent')
            conv = int(number)

            if conv > 0:
                countries[index].click()

                zones = driver.find_elements_by_xpath('//*[@id="main"]//td[2]/input')
                zones_list = []

                for zone in zones:
                    zones_names = zone.get_attribute('value')
                    zones_list.append(zones_names)
                sorted_zones_list = sorted(zones_list)

                m = 0
                zones_sorted = True

                for n in sorted_zones_list:
                    if n != zones_list[m]:
                        print('SORTED ZONES: ' + n + ', ORIGINAL ZONES: ' + zones_list[m])
                        zones_sorted = False
                    m += 1

                if not zones_sorted:
                    pass #print('Country' + countries[index] + ' has unsorted zones, DAMN IT!')

                #print(
                    #countries[index] + 'has' + countries_zone_nr[index] + 'zones!')  # << < HERE SKIP TO PREVIOUS PAGE`)
                zones_exist = True
                break

            index += 1

        index += 1

        if (zones_exist):
            driver.get(home)
            time.sleep(2)

        if (index > len(countries) - 1):  # zabezpiecznie przed petla nieskonczona
            still_finding_zones = False



    # j = 0
    # for nr in nr_zones:
    #     number = nr.get_attribute('textContent')
    #     conv = int(number)
    #
    #     if conv != 0:
    #         nr_countries[j].click()
    #
    #         zones = driver.find_elements_by_xpath('//*[@id="main"]//td[2]/input')
    #         zones_list = []
    #
    #         for zone in zones:
    #             zones_names = zone.get_attribute('value')
    #             zones_list.append(zones_names)
    #         sorted_zones_list = sorted(zones_list)
    #
    #         m = 0
    #         zones_sorted = True
    #
    #         for n in sorted_zones_list:
    #             if n != zones_list[m]:
    #                 print('SORTED ZONES: ' + n + ', ORIGINAL ZONES: ' + zones_list[m])
    #                 zones_sorted = False
    #             m += 1
    #
    #         if not zones_sorted:
    #             print('Country' + nr_countries[j] + ' has unsorted zones, DAMN IT!')
    #
    #         driver.get(home)
    #         time.sleep(2)
    #
    #
    #     j += 1



