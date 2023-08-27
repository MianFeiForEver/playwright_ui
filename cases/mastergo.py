from playwright.sync_api import Playwright, sync_playwright, Page, expect

from core.utils import create_page


def mg_login(page: Page) -> None:
    page.goto("/login")
    page.get_by_placeholder("手机号/邮箱").fill("1@1.data")
    page.get_by_placeholder("密码", exact=True).fill("111111")
    page.click(".label-check")
    page.get_by_role("button", name="开始使用").click()
    page.wait_for_load_state("networkidle")


def creat_file(page: Page) -> None:
    page.locator(".create-button-content").click()
    page.wait_for_load_state()
    page.locator("#canvas").click(position={"x": 414, "y": 200})
    page.wait_for_timeout(1000)

    page.keyboard.down("a")
    page.wait_for_timeout(1000)

    page.keyboard.up("a")
    page.get_by_text("iPhone 14 Pro Max").click()
    page.wait_for_timeout(1000)


def rm_files(page: Page) -> None:
    page.goto("/files/home")
    page.wait_for_load_state()
    files = page.locator(".item_container >div")
    files.first.wait_for()
    print("size:", files.count())
    while files.count():
        files.first.click(button="right")
        del_file = page.get_by_text("删除")
        rm_file = page.get_by_text("从主页移除")
        if expect(del_file.or_(rm_file)):
            print("两个元素存在")
            if del_file.is_visible():
                print("删除元素存在")
                del_file.click()
            else:
                print("从主页移除元素存在")
                rm_file.click()
        else:
            print("两个元素都不存在")
            break
    print("size:", files.count())


# 登录lanhu)
def run(playwright: Playwright) -> None:
    base_url = "https://mastergo.com/"
    page = next(create_page(playwright, base_url))
    mg_login(page)
    creat_file(page)
    rm_files(page)


with sync_playwright() as playwright:
    run(playwright)
