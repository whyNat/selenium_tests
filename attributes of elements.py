href = link.get_attribute("href")

driver.get('http://localhost/litecart/en/')
driver.find_element_by_css_selector('[name=query]').get_attribute('value')

driver.find_element_by_css_selector('#breadcrumbs a').get_attribute('href')  - szukanie po linku

driver.find_element_by_css_selector('[name=currency_code] [value=USD).get_attribute('selected')  - najpierw css, potem w nim value

