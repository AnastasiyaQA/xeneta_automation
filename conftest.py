from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome('/usr/bin')
    browser.maximize_window()
    return browser

