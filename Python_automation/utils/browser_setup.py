from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.config import load_config

def get_driver():
    config = load_config()
    browser = config['default']['browser']
    headless = config['default']['headless']

    if browser == 'chrome':
        options = ChromeOptions()
        if headless:
           options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    
    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    
    elif browser == 'edge':
        options = EdgeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Edge(options=options)
    
    else:
        raise Exception("Unsupported browser!")

    driver.implicitly_wait(config['default']['timeout'])
    return driver
