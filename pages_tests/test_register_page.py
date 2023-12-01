from selenium import webdriver
from selenium.webdriver.common.by import By
from confest import browser


def test_register_page(browser):
    driver = browser

    dropdown_elem = driver.find_element(by=By.CLASS_NAME, value='fa-user')
    dropdown_elem.click()

    dropdown_elem_contain = driver.find_element(by=By.CLASS_NAME, value='dropdown-menu-right')
    register_button = dropdown_elem_contain.find_element(by=By.TAG_NAME, value='a')
    register_button.click()

    assert driver.current_url == 'http://localhost/en-gb?route=account/register'
