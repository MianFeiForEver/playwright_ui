from core.utils import load_selectors


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "/sso/#/main/home"
        self.selectors = load_selectors("登录页")

    def navigate(self):
        self.page.goto(self.url)

    def fill_account(self, account):
        self.page.fill(self.selectors["账号输入框"], account)

    def fill_password(self, password):
        self.page.fill(self.selectors["密码输入框"], password)

    def check_agreement(self):
        self.page.click(self.selectors["用户协议框"])

    def click_login_button(self):
        self.page.click(self.selectors["登录按钮"])


class Login:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)

    def login_not_check(self, account, password):
        self.login_page.navigate()
        self.login_page.fill_account(account)
        self.login_page.click_login_button()

    def login_by_password(self, account, password):
        self.login_page.navigate()
        self.login_page.fill_account(account)
        self.login_page.check_agreement()
        self.login_page.click_login_button()
        self.login_page.fill_password(password)
        self.login_page.click_login_button()
        self.page.wait_for_load_state("networkidle")
        cookie = self.page.context.cookies()
        print(cookie)
