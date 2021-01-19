import time
from pytest import mark

from steps.demo_steps import submit_1to1_demo_request
from steps.demo_steps import submit_watch_now_request
from steps.demo_steps import submit_sign_up_here_request
from steps.demo_steps import open_demo_page
from steps.careers_steps import our_values_tabs_switching
from steps.careers_steps import open_careers_page
from steps.careers_steps import click_on_also_location
from steps.careers_steps import click_on_new_york_location
from steps.careers_steps import click_on_hamburg_location


@mark.test_demo_page_12
def test_request_1to1_demo(chrome_browser):
    open_demo_page(chrome_browser)
    submit_1to1_demo_request(chrome_browser)


@mark.test_demo_page_18
def test_request_watch_now_demo(chrome_browser):
    open_demo_page(chrome_browser)
    submit_watch_now_request(chrome_browser)


@mark.test_demo_page_27
def test_sign_up_here_demo(chrome_browser):
    open_demo_page(chrome_browser)
    submit_sign_up_here_request(chrome_browser)


@mark.test_careers_page_05
def test_switching_between_owr_values_tabs_careers(chrome_browser):
    open_careers_page(chrome_browser)
    our_values_tabs_switching(chrome_browser)


@mark.test_careers_page_09
def test_oslo_location_redirection(chrome_browser):
    open_careers_page(chrome_browser)
    click_on_also_location(chrome_browser)


@mark.test_careers_page_10
def test_new_york_location_redirection(chrome_browser):
    open_careers_page(chrome_browser)
    click_on_new_york_location(chrome_browser)


@mark.test_careers_page_11
def test_hamburg_location_redirection(chrome_browser):
    open_careers_page(chrome_browser)
    click_on_hamburg_location(chrome_browser)
