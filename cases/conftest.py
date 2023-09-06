import pytest
from playwright.sync_api import sync_playwright

from core.utils import storage_json


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized",
                                                          "--remote-debugging-port=9222",  # 配置远程调试端口
                                                          ], )

        yield browser
        browser.close()


@pytest.fixture(scope="session")
def context(browser, base_url):
    context = browser.new_context(base_url=base_url,
                                  bypass_csp=True, no_viewport=True,
                                  storage_state=storage_json,
                                  # record_video_dir="media/videos"
                                  )
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.expose_binding('browser', lambda: browser)

    yield context
    # context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
