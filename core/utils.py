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


cookies = [{'name': 'Hm_lvt_b4f3ed63ac4e8f18be586b41df007a16', 'value': '1693135917', 'domain': '.lanhuapp.com',
            'path': '/web/', 'expires': 1724671916, 'httpOnly': False, 'secure': False, 'sameSite': 'Lax'},
           {'name': 'Hm_lpvt_b4f3ed63ac4e8f18be586b41df007a16', 'value': '1693135917', 'domain': '.lanhuapp.com',
            'path': '/web/', 'expires': -1, 'httpOnly': False, 'secure': False, 'sameSite': 'Lax'},
           {'name': 'aliyungf_tc', 'value': '924fab9f37927a599a0e133c405e0398721ca9791cae9d2e08cad6b707414638',
            'domain': 'lanhuapp.com', 'path': '/', 'expires': -1, 'httpOnly': True, 'secure': False, 'sameSite': 'Lax'},
           {'name': 'acw_tc', 'value': '707c9f7216931359129498446e3dbb496829f30bd5441f6e3c176c2185b5b5',
            'domain': 'lanhuapp.com', 'path': '/', 'expires': 1693137713.082078, 'httpOnly': True, 'secure': False,
            'sameSite': 'Lax'},
           {'name': 'cbc', 'value': 'G26124AA03EFE8542AE16F841DF1B68EA562413FDA81C862063', 'domain': '.ynuf.aliapp.org',
            'path': '/', 'expires': 1724671914.014286, 'httpOnly': False, 'secure': True, 'sameSite': 'None'},
           {'name': 'PASSPORT',
            'value': 'ZTV6ZJK5EPOUBYOD3P7GNBUFKZA3GAIXAAQTV53CBWSMBNUAC7TTJ4B5NL5OACSYDPZL7HWZYEC6AQNFOQTJTUBGOFPTTM7O7VA3SBQ.39825E18BCEF34C86CCE88B96FDD5CCF9DA5A59F',
            'domain': 'lanhuapp.com', 'path': '/', 'expires': 1695727915.58502, 'httpOnly': True, 'secure': True,
            'sameSite': 'Lax'}, {'name': 'session',
                                 'value': '.eJyNkEtuHDEMRO_S6zQgUqQo-TIN_mQP7EwG7TG8MHz3aGBkH-0IqFCv3td2zDPfX7an-_mRv7bjEtvTFtRb4a4GBKMDsqeA-LBReuvYaOJU6F6Ng4g7uImG1KgSYk0xEGarwKPN9FKFTZ11hkmM3iAIfGSzRMeRoOFYmBgyZlAduC2QW56_9ZrX-z-0tz_Pl-vhL-mve1WlcIFdwGInZ9qNkNbJSNLAV93aAdjTeNXg7MNB0N1tdVuphov7OA5oo0LlASz1caLPKU4F1gd4LINZSXIJqEw1FtntM455uT7neTsvD7wttEURCWafqQqBxgRI-liHXFbofqrnj1yQnCaWOy9H-xKMu663o_oSMyDLzJX4eM_zJ_BfY7__AkI5gfM.F8zFqw.JmLLQ_RUfb9YVQSK9RQjbuJfgv0',
                                 'domain': '.lanhuapp.com', 'path': '/', 'expires': 1700911915.737069, 'httpOnly': True,
                                 'secure': False, 'sameSite': 'Lax'},
           {'name': '_bl_uid', 'value': '2vl7Xlz3tC4dCRe25q3Ieysit2Uz', 'domain': 'lanhuapp.com', 'path': '/',
            'expires': 1708687916.5865, 'httpOnly': False, 'secure': False, 'sameSite': 'Lax'},
           {'name': 'HMACCOUNT_BFESS', 'value': '73AED6C7669C1A25', 'domain': '.hm.baidu.com', 'path': '/',
            'expires': 1727695916.705675, 'httpOnly': False, 'secure': True, 'sameSite': 'None'}, {'name': 'user_token',
                                                                                                   'value': 'eyJhbGciOiJIUzI1NiIsImlhdCI6MTY5MzEzNTkxNiwiZXhwIjoxNzI0NjcxOTE2fQ.eyJpZCI6IjNhYTRkYzcxLTcxYmQtNGM1NC1iNDI0LTcxNTI0NzYxY2FjNSJ9.LGEKXripKgNfTJdnbyRoX4KOJp9HsLQuSAAucn3mtLQ',
                                                                                                   'domain': '.lanhuapp.com',
                                                                                                   'path': '/',
                                                                                                   'expires': 1695727917,
                                                                                                   'httpOnly': False,
                                                                                                   'secure': False,
                                                                                                   'sameSite': 'Lax'},
           {'name': 'SERVERID', 'value': '77063afb3331b1d79c928c9c0ccfd051|1693135918|1693135913',
            'domain': 'lanhuapp.com', 'path': '/', 'expires': -1, 'httpOnly': False, 'secure': False,
            'sameSite': 'Lax'}]


def set_cookies(page: Page):
    page.context.add_cookies(cookies)


def run_lighthouse(url):
    command = [
        '/Users/mac/PycharmProjects/playwright_ui/node_modules/.bin/lighthouse',
        url,
        '--output-format=json',
        '--output-path=./report.html'
    ]
    subprocess.run(command, shell=False, capture_output=True, text=True)
