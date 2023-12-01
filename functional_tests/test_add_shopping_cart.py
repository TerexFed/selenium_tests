import time   # без тайма не работает
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser


def test_add_shopping_cart(browser):
    driver = browser

    driver.execute_script("window.scrollTo(0, 500)")

    good = driver.find_element(by=By.CLASS_NAME, value='product-thumb')

    buttongroup = good.find_element(by=By.CLASS_NAME, value='button-group')
    button_add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(buttongroup.find_element(by=By.TAG_NAME, value='button'))
    )
    time.sleep(1)
    button_add_to_cart.click()

    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(1)
    result = driver.find_element(by=By.CLASS_NAME, value='btn-inverse')

    IsEqualizeDollar = result.text == '1 item(s) - $602.00'
    IsEqualizeEuro = result.text == '1 item(s) - 472.33€'
    assert IsEqualizeEuro or IsEqualizeDollar
