from selenium.webdriver.common.by import By
from conftest import browser


def test_change_currency(browser):
    driver = browser

    currency_change = driver.find_element(By.CLASS_NAME, 'dropdown-toggle')

    currency_change.click()

    list_of_currencies = driver.find_element(By.CLASS_NAME, 'dropdown-menu.show')

    euro_currency = list_of_currencies.find_element(By.TAG_NAME, 'li').find_element(By.TAG_NAME, 'a')
    euro_currency.click()

    current_currency = driver.find_element(by=By.CSS_SELECTOR, value='#form-currency > div > a > strong')

    assert current_currency.text == '€'
