from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage


class DemoPage(BasePage):
    url = 'https://www.xeneta.com/demo'

    @property
    def schedule_now_button(self):
        locator = (By.XPATH, '//div[@class="body-container-wrapper"]//a[@href="#form-popup-1"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def watch_now_button(self):
        locator = (By.XPATH, '//div[@class="body-container-wrapper"]//a[@href="#form-popup-2"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def sign_up_here(self):
        locator = (By.XPATH, '//div[@class="body-container-wrapper"]//a[@href="#form-popup-3"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    # Schedule Now Registration pop-up
    @property
    def first_name_input1(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=firstname]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def last_name_input1(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=lastname]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def company_name_input1(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=company]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def business_email_input1(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=email]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def phone_number_input(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=phone]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def job_title_input(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=jobtitle]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def company_type_select(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=type_of_prospect]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def privacy_policy_checkbox(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [name=confirm_opt_in]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def get_1to1_demo_button(self):
        locator = (By.CSS_SELECTOR, '#form-popup-1 [type=submit]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def confirmation_message1(self):
        locator = (By.CSS_SELECTOR, '[class="row-fluid"] #hs_form_target_form_900276728')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    # Watch now registration pop-up
    @property
    def first_name_input2(self):
        locator = (By.CSS_SELECTOR, '#form-popup-2 [name=firstname]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def last_name_input2(self):
        locator = (By.CSS_SELECTOR, '#form-popup-2 [name=lastname]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def company_name_input2(self):
        locator = (By.CSS_SELECTOR, '#form-popup-2 [name="company"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def business_email_input2(self):
        locator = (By.CSS_SELECTOR, '#form-popup-2 [name="email"]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def privacy_policy_checkbox2(self):
        locator = (By.CSS_SELECTOR, '#form-popup-2 [name=confirm_opt_in]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def watch_now_demo_button(self):
        locator = (By.CSS_SELECTOR, '#form-popup-2 [type=submit]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    # There is no confirmation message
    @property
    def confirmation_message2(self):
        locator = (By.CSS_SELECTOR, '[class="row-fluid"] #hs_form_target_form_900276728')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    # Sign Up Registration pop-up
    @property
    def first_name_input3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [name=firstname]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def last_name_input3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [name=lastname]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def company_name_input3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [name=company]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def business_email_input3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [name=email]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def job_title_input3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [name=jobtitle]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def company_type_select3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [name=type_of_prospect]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def privacy_policy_checkbox3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [name=confirm_opt_in]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def save_my_spot_button3(self):
        locator = (By.CSS_SELECTOR, '#form-popup-3 [type=submit]')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

    @property
    def confirmation_message3(self):
        locator = (By.CSS_SELECTOR, '[class="row-fluid"] #hs_form_target_form_415710560-1610644364272')
        return BaseElement(driver=self.driver, by=locator[0], value=locator[1])

