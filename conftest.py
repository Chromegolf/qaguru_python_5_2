import pytest
from selene import browser


@pytest.fixture(scope="session")
def set_browser():
    browser.config.window_width = 1366
    browser.config.window_height = 768
    browser.open('https://google.com')