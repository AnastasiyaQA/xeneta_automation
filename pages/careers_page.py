from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage


class CareersPage(BasePage):
    url = 'https://www.xeneta.com/careers'


    # Our values section elements

    @property
    def xeneta_is_one_tab(self):
        locator = (By.CSS_SELECTOR, '[data-tab="Xenetaisone-1"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def xeneta_is_one_content(self):
        locator = (By.ID, 'Xenetaisone-1')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def modernization_through_data_tab(self):
        locator = (By.CSS_SELECTOR, '[data-tab="Modernizationthroughdata-2"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def modernization_through_data_content(self):
        locator = (By.ID, 'Modernizationthroughdata-2')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def variety_and_fairness_tab(self):
        locator = (By.CSS_SELECTOR, '[data-tab="VarietyandFairness-3"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def variety_and_fairness_content(self):
        locator = (By.ID, 'VarietyandFairness-3')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def transparency_builds_trust_tab(self):
        locator = (By.CSS_SELECTOR, '[data-tab="TransparencybuildsTrust-4"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def transparency_builds_trust_content(self):
        locator = (By.ID, 'TransparencybuildsTrust-4')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    # Our locations section elements

    @property
    def oslo_location_widget(self):
        locator = (By.CSS_SELECTOR, '[class="card-content"] [href="https://www.xeneta.com/locations/oslo"] h4')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def new_york_location_widget(self):
        locator = (By.CSS_SELECTOR, '[class="card-content"] [href="https://www.xeneta.com/locations/new-york"] h4')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def hamburg_location_widget(self):
        locator = (By.CSS_SELECTOR, '[class="card-content"] [href="https://www.xeneta.com/locations/hamburg"] h4')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

