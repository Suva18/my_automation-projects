# Automation Projects
Welcome to the Automation Projects repository! This repository contains various automation projects built using different tools and frameworks such as Python with Cucumber, Playwright, aiTest, and Selenium. Each project is organized into its own directory with clear instructions on how to set up, run, and expand the automation tests.

# Repository Structure
**PythonCucumberAutomation**
Automation testing using Python Cucumber for BDD style testing.
**Python_automation**
A set of Python scripts for automation testing, using Selenium for UI automation.
**aiTest_python_automation**
Automation with aiTest, leveraging AI-driven test features.
**playwright-automation**
Playwright automation scripts for end-to-end browser testing.
**.gitignore**
Ensures sensitive and unnecessary files are not committed to the repository.

# Getting Started
Follow the instructions below to set up and run each of the automation projects.
**Prerequisites**
Python 3.x installed on your machine
Git for cloning the repository
A package manager like pip for installing dependencies
Web browsers (Chrome, Firefox, Edge) for Playwright automation
IDE (like PyCharm or VS Code) for coding and running tests
**1. Python Cucumber Automation**
This project uses Python with Cucumber for Behavior-Driven Development (BDD).
Installation
**Clone the repository**
git clone https://github.com/Suva18/my_automation-projects
**Navigate to the project folder**
cd PythonCucumberAutomation
**Install required dependencies**
` pip install -r requirements.txt `
How to Run Tests
Update the feature files under features/ directory.
Execute the tests using the command:
`behave`
**Key Features**
BDD Framework: Easy-to-understand syntax using Gherkin for behavior-driven development.
Report generation: Automatically generate test reports after execution.

**2. Python Automation**
This project is centered around Selenium automation scripts for web applications.
Installation
**Navigate to the project folder**
cd Python_automation
**Install dependencies**
` pip install -r requirements.txt `
How to Run Tests
Update the test cases under tests/ directory.
Execute tests using pytest:
` pytest `
Key Features
Cross-browser testing: Supports Chrome, Firefox, and other major browsers.
Test Reporting: Detailed HTML reports after each run.

**3. aiTest Python Automation**
This project uses aiTest for AI-driven testing automation.
Installation
**Navigate to the project folder**
cd aiTest_python_automation
**Install dependencies**
` pip install -r requirements.txt `
How to Run Tests
Ensure your aiTest environment is properly set up.
Execute the tests using your aiTest CLI commands:
` pytest `
Key Features
AI-powered tests: Test cases enhanced with AI for more dynamic automation.
Self-healing tests: Auto-correction for broken tests.

**4. Playwright Automation**
The Playwright project is used for end-to-end browser automation testing.
Installation
**Navigate to the project folder**
cd playwright-automation
**Install dependencies**
` npm install `
How to Run Tests
Run tests on all supported browsers:
` npx playwright test `
View the HTML report for detailed results:
` npx playwright show-report `
Key Features
Cross-browser testing: Supports Chrome, Firefox, and Edge.
HTML Reports: Detailed reports with test results.
Headless Testing: Faster test execution by running in headless mode.

**.gitignore**
This file ensures that unnecessary files are not committed to the repository, such as:

**Python virtual environments**
Node modules
Log files
OS-specific files (e.g., .DS_Store)
Contributing
Feel free to open issues or contribute by creating a pull request for bug fixes or new features. Ensure all tests pass before submitting.
