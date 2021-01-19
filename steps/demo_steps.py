from pages.demo_page import DemoPage
from selenium.webdriver.support import expected_conditions as EC

from test_data import TestData


def open_demo_page(chrome_browser):

    demo_page = DemoPage(driver=chrome_browser)

    # Open page url
    demo_page.go()

    # Click 'Yes, I'm happy' button for accepting cookie policy
    demo_page.accept_cookies_button.click()


def submit_1to1_demo_request(chrome_browser):

    # Load test data from json
    test_data = TestData("registrationFrom1")

    demo_page = DemoPage(driver=chrome_browser)

    # Click 'Schedule Now' button on demo page
    demo_page.schedule_now_button.click()

    # Insert test data in required fields on registration form
    demo_page.first_name_input1.input_text(test_data.firstName)
    demo_page.last_name_input1.input_text(test_data.lastName)
    demo_page.company_name_input1.input_text(test_data.companyName)
    demo_page.business_email_input1.input_text(test_data.email)
    demo_page.phone_number_input.input_text(test_data.phone)
    demo_page.job_title_input.input_text(test_data.jobTitle)
    demo_page.company_type_select.select_by_value(test_data.companyType)
    demo_page.privacy_policy_checkbox.click()

    # Submit registration form
    demo_page.get_1to1_demo_button.click()

    # TEST -> That confirmation message is displayed, after submitting 1 to 1 demo request form
    assert EC.visibility_of_element_located(demo_page.confirmation_message1)


def submit_watch_now_request(chrome_browser):

    # Load test data from json
    test_data = TestData("registrationFrom2")

    demo_page = DemoPage(driver=chrome_browser)

    # Click 'Watch Now' button on demo page
    demo_page.watch_now_button.click()

    # Insert test data in required fields on registration form
    demo_page.first_name_input2.input_text(test_data.firstName)
    demo_page.last_name_input2.input_text(test_data.lastName)
    demo_page.company_name_input2.input_text(test_data.companyName)
    demo_page.business_email_input2.input_text(test_data.email)
    demo_page.privacy_policy_checkbox2.click()

    # Submit registration form
    demo_page.watch_now_demo_button.click()

    # TEST -> That confirmation message is displayed, after submitting watch now request form
    assert EC.visibility_of_element_located(demo_page.confirmation_message2)


def submit_sign_up_here_request(chrome_browser):

    # Load test data from json
    test_data = TestData("registrationFrom3")

    demo_page = DemoPage(driver=chrome_browser)

    # Click 'Sign Up Here' button on demo page
    demo_page.sign_up_here.click()

    # Insert test data in required fields on registration form
    demo_page.first_name_input3.input_text(test_data.firstName)
    demo_page.last_name_input3.input_text(test_data.lastName)
    demo_page.company_name_input3.input_text(test_data.companyName)
    demo_page.business_email_input3.input_text(test_data.email)
    demo_page.job_title_input3.input_text(test_data.jobTitle)
    demo_page.company_type_select3.select_by_value(test_data.companyType)
    demo_page.privacy_policy_checkbox3.click()

    # Submit registration form
    demo_page.save_my_spot_button3.click()

    # TEST -> That confirmation message is displayed, after submitting sign up form
    assert EC.visibility_of_element_located(demo_page.confirmation_message3)



