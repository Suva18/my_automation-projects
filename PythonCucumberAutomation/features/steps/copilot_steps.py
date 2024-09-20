from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I am on the Copilot page')
def step_impl(context):
     context.browser.get(context.base_url + "/copilot")

@when('I perform a Copilot action')
def step_impl(context):
    copilot_button = context.browser.find_element(By.XPATH, "//button[@aria-label='Copilot']")
    copilot_button.click()

@then('I should see the expected result')
def step_impl(context):
    result = context.browser.find_element(By.ID, 'result')
    assert result.is_displayed()
