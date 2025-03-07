import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def setup_browser():
    browser.config.driver_options = webdriver.ChromeOptions()
    #browser.config.driver_options.add_argument('--headless')
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    yield
    browser.quit()