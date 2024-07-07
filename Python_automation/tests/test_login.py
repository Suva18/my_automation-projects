import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("suvarna.kanawade@appliedaiconsulting.com")
        login_page.enter_password("Suvarna@1897")
        login_page.click_login()
        
        # Wait for the title to contain "URL Test" for up to 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("URL Test"),
            "Login successful but Title does not contain 'URL Test'."
        )
        
        # Assert that the title contains "URL Test"
        assert "URL Test" in self.driver.title, "Login successful but title does not match expected."
    

