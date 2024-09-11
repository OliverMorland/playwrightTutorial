import pytest
from playwright.sync_api import Playwright

from pom.seti_sadoc_login_page import SetiSadocLoginPage


@pytest.fixture(scope="function")
def single_set_up(page):
    yield page
    page.close()


@pytest.fixture(scope="session")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page


@pytest.fixture(scope="session")
def login_set_up(set_up):
    page = set_up
    login_page = SetiSadocLoginPage(page)
    login_page.navigate()
    login_page.login("SADOCSETIuser@hendall.com")
    yield login_page.page
