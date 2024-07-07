# aiTest Automation Framework
The aiTest Python automation framework is designed to automate the testing of the aiTest web application using Selenium. This framework supports multiple browsers (Chrome, Edge, Firefox) in headless mode and includes reporting support.

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Writing Test Cases](#writing-test-cases)
- [Generating Reports](#generating-reports)
- [Contributing](#contributing)

## Overview
This automation framework is designed for testing the aiTest web application using Python and Selenium. It includes a Page Object Model (POM) structure for better code organization and maintenance.

## Setup
### Prerequisites
Before setting up the project, make sure you have the following installed:
- Python (version >= 3.6)
- Chrome , Firefox and Edge browser (depending on your WebDriver choice)

### Installation
#### 1.Set Up a Virtual Environment
i. Create a Project Directory:
    `mkdir aiTest_python_automation`
   `cd aiTest_python_automation`
ii. Create a Virtual Environment:
    `python -m venv venv`
iii. Activate the Virtual Environment:
    `venv\Scripts\activate`
#### 2.Install Required Packages
i. Install Selenium and pytest:
`pip install selenium pytest pytest-html`
ii. Create a requirements.txt file:
`echo selenium >> requirements.txt`
`echo pytest >> requirements.txt`
`echo pytest-html >> requirements.txt`

#### 3.Set Up Project Structure 
i. Create Directory Structure:
`mkdir tests pages reports utils test_data`
ii. Create __init__.py in Each Directory:
`type NUL > tests\__init__.py`
`type NUL > pages\__init__.py`
`type NUL > utils\__init__.py`
type NUL > test_data\__init__.py

## Project Structure

aiTest_automation/
│
├── tests/
│ ├── test_login.py
│ ├── test_signup.py
│ └── init.py
│
├── pages/
│ ├── login_page.py
│ ├── signup_page.py
│ └── init.py
│
├── reports/
│ └── (auto-generated report files)
│
├── utils/
│ ├── browser_setup.py
│ ├── config.py
│ └── init.py
│
├── test_data/
│ ├── login_data.json
│ ├── signup_data.json
│ └── init.py
│
├── .gitignore
├── requirements.txt
├── config.yaml
├── conftest.py
└── README.md

## Usage
#### 1.Create Page Object Model (POM) Classes
Create login_page.py in pages:
##### Code Snippets for Reference
Refer the code snippet below:
`pages/login_page.py`
<pre>
  <code class="python">
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login")
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    </code>
</pre>

#### 2.Configure Web Drivers and Browser Setup
Download the web drivers for Chrome, Edge, and Firefox, and add them to your system's PATH.
Create browser_setup.py in utils
``` utils/browser_setup.py ```
Project Configuration
Set the default browser in the config.yaml file:
``` default_browser: chrome ```

#### 3.Add Test Data
##### Sample code snippet:
`Create login_data.json in test_data`
{
    "valid_user": "test_user",
    "valid_pass": "test_password"
}
#### 4.Load Configuration Data
##### Sample code snippet:
`Create config.py in utils`
<pre>
  <code class="python">
#utils/config.py
import yaml
import os
def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config
def get_browser():
    config = load_config()
    return os.getenv('BROWSER', config.get('default_browser', 'chrome'))
    </code>
</pre>
    
#### 5.Integrate Everything
##### Sample code snippet:
`Create conftest.py in the root directory`
<pre>
  <code class="python">
import pytest
from utils.browser_setup import get_driver
from utils.config import get_browser
@pytest.fixture(scope="session")
def browser():
    return get_browser()
@pytest.fixture(scope="class")
def setup(request, browser):
    driver = get_driver(browser)
    request.cls.driver = driver
    yield
    driver.quit()
    </code>
</pre>

## Writing Test Cases
Place your test files in the tests directory.
Use the setup fixture to initialize the browser driver.
Organize your page objects in the pages directory.
#### Example Test File
Refer the  Example Test File below:
`tests/test_login.py`
<pre>
  <code class="python">
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        self.driver.get("https://app.aitest.qualityx.io/url-test")
        login_page = LoginPage(self.driver)
        login_page.enter_username("valid_user")
        login_page.enter_password("valid_pass")
        login_page.click_login()
        assert "Dashboard" in self.driver.title
    </code>
</pre>
    
## Run Tests with Report Generation
Test results are generated in the reports directory. Use pytest-html to create HTML reports:
``` pytest --html=reports/report.html ```

## Contributing
We welcome contributions! Please submit issues or pull requests if you have suggestions or improvements.
This README provides a comprehensive overview of the aiTest Python automation framework, including the project structure, setup instructions, test writing guidelines, and reporting features.







