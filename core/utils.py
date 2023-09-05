import json
import subprocess

from playwright.async_api import Page
from ruamel.yaml import YAML


def load(path):
    with open(path, encoding="utf-8") as f:
        yaml = YAML(typ="safe")
        return yaml.load(f)


def load_selectors(page_name):
    return load("../data/elements/lanhu.yaml").get(page_name)


def zoom(page, numbers):
    for _ in range(numbers):
        page.keyboard.down("Control")
        page.keyboard.press("0")
        page.wait_for_timeout(100)
        for i in range(4):
            page.mouse.wheel(0, 100)
        page.keyboard.press("0")
        page.wait_for_timeout(100)
        for i in range(4):
            page.mouse.wheel(0, -100)


cookies = [{'name': 'PASSPORT',
            'value': 'ZTV6ZJK5EPOUBYOD3P7GNBUFKZA3GAIXAAQTV53CBWSMBNUAC7TTJ4B5NL5OACSYDPZL7HWZYEC6AQNFOQTJTUBGOFPTTM7O7VA3SBQ.39825E18BCEF34C86CCE88B96FDD5CCF9DA5A59F',
            'domain': 'lanhuapp.com', 'path': '/', 'expires': 1695727915.58502, 'httpOnly': True, 'secure': True,
            'sameSite': 'Lax'},
           {'name': 'session',
            'value': '.eJyNkEtuHDEMRO_S6zQgUqQo-TIN_mQP7EwG7TG8MHz3aGBkH-0IqFCv3td2zDPfX7an-_mRv7bjEtvTFtRb4a4GBKMDsqeA-LBReuvYaOJU6F6Ng4g7uImG1KgSYk0xEGarwKPN9FKFTZ11hkmM3iAIfGSzRMeRoOFYmBgyZlAduC2QW56_9ZrX-z-0tz_Pl-vhL-mve1WlcIFdwGInZ9qNkNbJSNLAV93aAdjTeNXg7MNB0N1tdVuphov7OA5oo0LlASz1caLPKU4F1gd4LINZSXIJqEw1FtntM455uT7neTsvD7wttEURCWafqQqBxgRI-liHXFbofqrnj1yQnCaWOy9H-xKMu663o_oSMyDLzJX4eM_zJ_BfY7__AkI5gfM.F8zFqw.JmLLQ_RUfb9YVQSK9RQjbuJfgv0',
            'domain': '.lanhuapp.com', 'path': '/', 'expires': 1700911915.737069, 'httpOnly': True,
            'secure': False, 'sameSite': 'Lax'},
           ]


def set_cookies(page: Page):
    page.context.add_cookies(cookies)


js_cookies = json.dumps(cookies)


def run_lighthouse(url):
    command = ['lighthouse', f"'{url}'",
               '--port=9222',
               '--output=json',
               '--extra-headers', f'cookie: {cookies}'
               '--output-path=./report.html'
               ]
    subprocess.call(' '.join(command), shell=True)