from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import browser


def test_cart_page_empty(browser):
    driver = browser

    open_cart_button = driver.find_element(by=By.CSS_SELECTOR, value='#top > div > div.nav.float-end > ul > '
                                                                     'li:nth-child(4) > a')
    open_cart_button.click()
    driver.implicitly_wait(2)

    content = driver.find_element(by=By.ID, value='content')
    result = content.find_element(by=By.TAG_NAME, value='p').text

    assert result == 'Your shopping cart is empty!'
