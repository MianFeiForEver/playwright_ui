import pytest
from playwright.sync_api import Page

from data.pages.mg.login import Login


def test_login(page: Page):
    login = Login(page)
    login.login_by_password("1@1.lanhu", "111111")
    with pytest.assume:
        assert page.title() == "主页 - MasterGo"
