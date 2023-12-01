from selenium import webdriver
from selenium.webdriver.common.by import By
from confest import browser


def test_wishlist_page(browser):
    driver = browser

    open_wishlist_button = driver.find_element(by=By.ID, value='wishlist-total')
    open_wishlist_button.click()

    assert driver.current_url == 'http://localhost/en-gb?route=account/wishlist'

    time.sleep(1)
