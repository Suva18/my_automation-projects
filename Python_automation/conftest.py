import pytest
from utils.browser_setup import get_driver
from utils.test_data import load_test_data

@pytest.fixture(scope="class")
def setup(request):
    driver = get_driver()
    test_data = load_test_data()
    base_url = test_data['base_url']
    driver.get(base_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


