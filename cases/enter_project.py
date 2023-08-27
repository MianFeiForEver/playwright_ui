from playwright.sync_api import Page

from data.pages.lanhu.login import Login
from data.pages.lanhu.project import Project


def test_login_fail(page: Page):
    login = Login(page)
    login.login_not_check("15011290391", "123456789")


def test_login_success(page: Page):
    login = Login(page)
    login.login_by_password("15011290391", "12345678")


def test_run(page: Page):
    project = Project(page)
    project.zoom(10)
