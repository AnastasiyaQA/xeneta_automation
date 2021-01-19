from selenium.webdriver.common.by import By
from .base_element import BaseElement


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    @property
    def close_chat_button(self):
        locator = (By.CSS_SELECTOR, '[data-test-id="initial-message-close-button"] svg')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def accept_cookies_button(self):
        locator = (By.CSS_SELECTOR, "#hs-en-cookie-confirmation-buttons-area #hs-eu-confirmation-button")
        return BaseElement(self.driver, by=locator[0], value=locator[1])
