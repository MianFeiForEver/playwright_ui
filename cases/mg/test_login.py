import pytest
from playwright.sync_api import Page, APIResponse, expect

from data.pages.mg.login import Login

login_res = APIResponse


def intercept_request(route, request):
    global login_res
    login_res = route.fetch()


def test_login(page: Page):
    login = Login(page)
    page.route("/api/v1/signin", intercept_request)
    login.login_by_password("1@1.lanhu", "111111")
    with pytest.assume:
        assert login_res.status == 200, "状态码错误"
    print(login_res.status)
    expect(login_res).to_be_ok()
    print("测试完成")
