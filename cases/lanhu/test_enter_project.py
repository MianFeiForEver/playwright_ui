from playwright.sync_api import Page

from core.utils import add_cookies
from data.pages.lanhu.login import Login
from data.pages.lanhu.project import Project


def test_login_fail(page: Page):
    login = Login(page)
    login.login_not_check("15011290391", "123456789")


def test_login_success(page: Page):
    login = Login(page)
    login.login_by_password("15011290391", "12345678")


def test_run(page: Page):
    add_cookies(page)
    project = Project(page)
    project.zoom(2)
