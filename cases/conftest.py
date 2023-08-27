import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"], )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser, base_url):
    context = browser.new_context(base_url=base_url,
                                  bypass_csp=True, no_viewport=True,
                                  storage_state="config/auth/state.json",
                                  # record_video_dir="media/videos"
                                  )
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    # context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
