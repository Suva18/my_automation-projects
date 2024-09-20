# login_steps.py

from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage  # Adjust import based on your project structure

@given('I am on the login page')
def step_impl(context):
    context.browser.get(context.base_url)

@when('I enter the username "{username}"')
def step_impl(context, username):
    login_page = LoginPage(context.browser)
    login_page.enter_username(username)

@when('I enter the password "{password}"')
def step_impl(context, password):
    login_page = LoginPage(context.browser)
    login_page.enter_password(password)

@when('I click the login button')
def step_impl(context):
    login_page = LoginPage(context.browser)
    login_page.click_login()

@then('I should see the title containing "{title}"')
def step_impl(context, title):
    WebDriverWait(context.browser, 10).until(
        EC.title_contains(title),
        f"Login successful but Title does not contain '{title}'."
    )
    assert title in context.browser.title, f"Login successful but title does not match expected."
