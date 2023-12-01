import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser():
    options = Options()
    service = Service()
    driver = webdriver.Chrome(options, service)
    driver.get("http://localhost/")
    driver.implicitly_wait(1)
    yield driver
    driver.quit()
