from pages.careers_page import CareersPage
from selenium.webdriver.support import expected_conditions as EC


def open_careers_page(chrome_browser):
    careers_page = CareersPage(driver=chrome_browser)

    # Open page url
    careers_page.go()

    # Click 'Yes, I'm happy' button for accepting cookie policy
    careers_page.accept_cookies_button.click()


def our_values_tabs_switching(chrome_browser):
    careers_page = CareersPage(driver=chrome_browser)

    careers_page.xeneta_is_one_tab.click()

    # TEST -> That 'Xeneta is one' section is displayed when click on 'Xeneta is one' tab
    assert EC.invisibility_of_element(careers_page.xeneta_is_one_content)

    careers_page.modernization_through_data_tab.click()

    # TEST -> That 'Modernization through data' section is displayed when click on 'Modernization through data' tab
    assert EC.invisibility_of_element(careers_page.modernization_through_data_content)

    careers_page.variety_and_fairness_tab.click()

    # TEST -> That 'Variety and fairness' section is displayed when click on 'Variety and fairness' tab
    assert EC.invisibility_of_element(careers_page.variety_and_fairness_content)

    careers_page.transparency_builds_trust_tab.click()

    # TEST -> That 'Transparency builds trust' section is displayed when click on 'Transparency builds trust' tab
    assert EC.invisibility_of_element(careers_page.transparency_builds_trust_tab)


def click_on_also_location(chrome_browser):
    careers_page = CareersPage(driver=chrome_browser)

    # Click on Oslo widget on Careers page
    careers_page.oslo_location_widget.click()

    # TEST -> That web page with OSLO location description is opened
    assert chrome_browser.current_url == 'https://www.xeneta.com/locations/oslo'


def click_on_new_york_location(chrome_browser):
    careers_page = CareersPage(driver=chrome_browser)

    # Click on New York widget on Careers page
    careers_page.new_york_location_widget.click()

    # TEST -> That web page with New York location description is opened
    assert chrome_browser.current_url == 'https://www.xeneta.com/locations/new-york'


def click_on_hamburg_location(chrome_browser):
    careers_page = CareersPage(driver=chrome_browser)

    # Click on Hamburg widget on Careers page
    careers_page.hamburg_location_widget.click()

    # TEST -> That web page with Hamburg location description is opened
    assert chrome_browser.current_url == 'https://www.xeneta.com/locations/hamburg'


