from pytest import fixture

from selenium import webdriver


@fixture(scope='function')
def firefox_browser():
    browser = webdriver.Firefox()
    return browser
