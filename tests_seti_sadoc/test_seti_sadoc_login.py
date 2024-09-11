import time

import pytest
from playwright.sync_api import expect

from pom.seti_sadoc_login_page import SetiSadocLoginPage


def test_seti_sadoc_login(login_set_up) -> None:
    # page = set_up
    # login_page = SetiSadocLoginPage(page)
    # login_page.navigate()
    # login_page.login("SADOCSETIuser@hendall.com")
    login_page = login_set_up
    expect(login_page.get_by_role("button", name="Logout")).to_be_visible()

    # ---------------------


@pytest.mark.parametrize("email", ["SADOCSETIuser@hendall.com",
                                   pytest.param("fake@hendall.com", marks=pytest.mark.xfail)])
def test_seti_sadoc_login_works(single_set_up, email) -> None:
    page = single_set_up
    login_page = SetiSadocLoginPage(page)
    login_page.navigate()
    login_page.login(email)
    expect(login_page.page.get_by_role("button", name="Logout")).to_be_visible()
