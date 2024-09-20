from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            username_field.clear()
            username_field.send_keys(username)
        except Exception as e:
            print(f"Exception occurred while entering username: {e}")
            raise

    def enter_password(self, password):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password_field.clear()
            password_field.send_keys(password)
        except Exception as e:
            print(f"Exception occurred while entering password: {e}")
            raise

    def click_login(self):
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign-In']"))
            )
            login_button.click()
        except Exception as e:
            print(f"Exception occurred while clicking login button: {e}")
            raise
