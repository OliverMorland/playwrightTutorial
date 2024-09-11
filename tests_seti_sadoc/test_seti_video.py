import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.seti_sadoc_login_page import SetiSadocLoginPage


def test_seti_video(login_set_up) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = set_up
    # login_page = SetiSadocLoginPage(page)
    # login_page.navigate()
    # login_page.login("SADOCSETIuser@hendall.com")
    page = login_set_up
    page.get_by_role("link", name="Past Events").click()
    page.get_by_role("link", name="2023 SETI Training", exact=True).click()
    page.get_by_role("link", name="Video Library").click()
    page.get_by_role("link", name="Watch Video (High Bandwidth)").first.click()

    # ---------------------
    # context.close()
    # browser.close()
