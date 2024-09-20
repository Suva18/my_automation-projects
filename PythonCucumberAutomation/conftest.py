 # conftest.py

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.aitest.qualityx.io/")  # Replace with the actual login page URL
    yield driver
    driver.quit()

