from core.js_handle import start_js, end_js
from core.utils import zoom


class ProjectPage:
    def __init__(self, page):
        self.page = page
        self.url = "/web/#/item/project/stage?tid=6ac736f1-2a7f-4eb7-9a54-c68402aa9233&pid=61030b35-2ece-4575-9fd5-6bc799f3a95c"

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def click_canvas(self):
        self.page.locator("canvas").nth(1).click()


class Project:
    def __init__(self, page):
        self.page = page
        self.project_page = ProjectPage(self.page)

    def zoom(self, numbers):
        # set_cookies(self.page)
        self.project_page.navigate()
        self.page.evaluate(start_js())
        self.project_page.click_canvas()
        a = zoom(self.page, numbers)
        self.page.evaluate(end_js())

        # run_lighthouse(self.page.url)
