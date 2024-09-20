from behave import given, when, then

@given('I navigate to the homepage')
def step_impl(context):
    context.browser.get(context.config['https://app.aitest.qualityx.io/'])

@then('the title should be "{title}"')
def step_impl(context, title):
    assert context.browser.title == title
