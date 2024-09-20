# test_copilot.py

import pytest
from selenium.webdriver.common.by import By  # Add this import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("browser")  # Ensure the correct fixture name is used
def test_copilot(browser):  # Adjust the test function to use 'browser'
    browser.get("https://app.aitest.qualityx.io/")
    #copilot_button = browser.find_element(By.ID, 'copilot-button')

    # Example assertion or further actions
    #assert copilot_button.is_displayed(), "Copilot button is not displayed"
