import time
from lib2to3.pgen2.grammar import line

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
    #WebDriverWait(driver, 240000).until(EC.title_is('My Store'))
    time.sleep(4)
    home = driver.current_url


    not_all_main_link_clicked = True
    main_link = 0

    while not_all_main_link_clicked:

        list_of_main_links = driver.find_elements_by_css_selector('#app- a')


        for link in list_of_main_links:
            link.click()

            not_all_sub_link_clicked = True
            sub_link = 0

            while not_all_sub_link_clicked:

                list_of_sublinks = driver.find_elements_by_css_selector('ul.docs a')

                for link2 in list_of_sublinks:
                    link2.click()
                    title2 = driver.find_element_by_tag_name('h1')
                    h1_2 = title2.get_attribute('textContent')
                    h1_2 = h1_2.lstrip('\n ')
                    link_name2 = driver.find_element_by_css_selector('ul.docs span.name')
                    link_name2_text = link_name2.get_attribute('textContent')
                    if h1_2 == link_name2_text:
                        print('Title is equal to the link name')
                    else:
                        print('There\'s sth wrong')

            sub_link += 1


            title = driver.find_element_by_tag_name('h1')
            h1 = title.get_attribute('textContent')
            link_name = link.get_attribute('textContent')
            if h1 == link_name:
                print('Title is equal to the link name')
            else:
                print('There\'s sth wrong')

    main_link += 1

    driver.get(home)


