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
    session = page.context.new_cdp_session(page)
    session.send("Overlay.setShowFPSCounter", {"show": True})

    session.send('Performance.enable')
    login = Login(page)
    login.login_by_password("15011290391", "12345678")

    project = Project(page)
    project.zoom(2)
    report = session.send("Performance.getMetrics").get("metrics")
    report_dict = {}
    for item in report:
        report_dict[item["name"]] = item["value"]
    tti = report_dict["NavigationStart"] + report_dict["ProcessTime"]
    ctti = report_dict["DomContentLoaded"] + report_dict["ProcessTime"]
    print("tti", round(tti / 1000, 2))
    print("ctti", round(ctti / 1000, 2))

    # run_lighthouse(page.url)
