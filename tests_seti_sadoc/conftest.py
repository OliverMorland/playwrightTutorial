import os
import time

import pytest
from playwright.sync_api import Playwright
from pom.seti_sadoc_login_page import SetiSadocLoginPage

SETI_SADOC_LOGIN = os.environ["SETI_SADOC_LOGIN"]


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
def create_context(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    login_page = SetiSadocLoginPage(page)
    login_page.navigate()
    login_page.login(SETI_SADOC_LOGIN)
    yield context


@pytest.fixture()
def login_set_up(create_context):
    context = create_context
    page = context.new_page()
    page.set_default_timeout(3000)
    page.goto("https://uat.qsep.cms.gov/Events/EventHome.aspx?event=SETISADOC")
    # login_page = SetiSadocLoginPage(page)
    # login_page.navigate()
    # login_page.login(SETI_SADOC_LOGIN)
    yield page
