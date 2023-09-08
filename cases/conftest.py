import pytest

from core.utils import storage_json


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args, browser_name):
    if browser_name == "chromium":
        args = ["--start-maximized", "--remote-debugging-port=9222", ]
    else:
        args = []
    return {**browser_type_launch_args, "args": args, }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "storage_state": storage_json, "no_viewport": True, "bypass_csp": True,
            "ignore_https_errors": True,
            # "record_video_dir": home() + "/media/videos"
            }


@pytest.fixture(scope="function")
def context(browser_type, pytestconfig, browser_type_launch_args, browser_context_args):
    browser = browser_type.launch(**browser_type_launch_args)
    context = browser.new_context(
        **browser_context_args
    )
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.set_default_timeout(60000)
    yield context
    # context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
