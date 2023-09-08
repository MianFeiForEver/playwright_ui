from playwright.sync_api import Page

from core.utils import load_selectors


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "/login"
        self.selectors = load_selectors("登录页")

    def navigate(self):
        self.page.goto(self.url)

    def fill_account(self, account):
        self.page.get_by_placeholder("手机号/邮箱").fill(account)

    def fill_password(self, password):
        self.page.get_by_placeholder("密码", exact=True).fill(password)

    def check_agreement(self):
        self.page.click(".label-check")

    def click_login_button(self):
        self.page.get_by_role("button", name="开始使用").click()


class Login:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
        self.login_page.navigate()
        self.page.wait_for_timeout(1000)

    def login_not_check(self, account, password):
        self.login_page.fill_account(account)
        self.login_page.click_login_button()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_load_state("domcontentloaded")

    def login_by_password(self, account, password):
        # self.page.on("response", handle)

        self.login_page.fill_account(account)
        self.login_page.fill_password(password)
        self.login_page.check_agreement()
        # Use a regular expression
        self.login_page.click_login_button()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_load_state("domcontentloaded")

        # self.page.wait_for_load_state("networkidle")
        # cookie = self.page.context.cookies()
