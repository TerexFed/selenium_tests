from selenium.webdriver.common.by import By
from confest import browser


def test_phone_search(browser):
    driver = browser

    search_elem = driver.find_element(by=By.NAME, value='search')
    search_elem.send_keys('phone')

    send_button = driver.find_element(by=By.CLASS_NAME, value='btn-light')
    send_button.click()

    content_block = driver.find_element(by=By.ID, value='content')
    search_result = content_block.find_element(by=By.TAG_NAME, value='h1')

    assert search_result.text == 'Search - phone'
