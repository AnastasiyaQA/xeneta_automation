from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    browser.maximize_window()
    return browser

