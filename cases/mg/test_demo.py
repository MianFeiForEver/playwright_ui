import pytest
from playwright.sync_api import Page

from core.utils import save_params
from data.pages.mg.login import Login


# 测试demo 登录成功,断言title
def test_demo(page: Page):
    login = Login(page)
    login.login_by_password("1@1.lanhu", "111111")
    with pytest.assume:
        assert page.title() == "主页 - MasterGo"


# 测试demo 登录成功,断言接口返回信息
def test_demo_route(page: Page):
    login = Login(page)
    api_rqs = {}

    def handle(response):
        if response is not None:
            if response.url.endswith("/api/v1/user"):
                api_rqs["user"] = response

    page.on("response", handle)
    login.login_by_password("1@1.lanhu", "111111")

    with pytest.assume:
        assert api_rqs["user"].status == 200, "状态码错误"
        assert api_rqs["user"].json()["code"] == "OK", "code错误"
    save_params("email", api_rqs["user"].json()["data"]["email"])
    save_params("user_id", api_rqs["user"].json()["data"]["id"])
