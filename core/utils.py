import argparse
import json
import subprocess
from pathlib import Path

from configobj import ConfigObj
from playwright.async_api import Page
from ruamel.yaml import YAML


def home():
    """
    获取项目根目录
    :return:
    """
    print("****")
    return Path(__file__).parent.parent.__str__()


def get_ini():
    return ConfigObj("pytest.ini", encoding="UTF8")


def load(path):
    with open(path, encoding="utf-8") as f:
        yaml = YAML(typ="safe")
        return yaml.load(f)


def load_selectors(page_name):
    return load(home() + "/data/elements/lanhu.yaml").get(page_name)


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


cookies = [{
    "name": "PASSPORT",
    "value": "QBTRPFFW7IIPKHIVVPUPBB2NMR6DQSCQSW3GPFKYS22RZLIAMDJTKTNI6TDV4BFFXP3EVUBR4VLWAR4GGSSYGQRKHKGUVY6X5P6QEHQ.DC0FA4601974B5C8A6D29881BEEA6855E3324893",
    "domain": "lanhuapp.com",
    "path": "/",
    "sameSite": "Lax"
},
    {
        "name": "session",
        "value": ".eJyNkMFKBEEMRP9lzg500kkn488MnXSii7ou44oH8d_tZfHurQqq4FV9L3se8fG8PF6Pz3hY9tNYHhcnN8tQE6xDrXepaA1CxZQFUWuRohY4slZGZCKMjppdtVWV6UwbZ3iyW1UtolaBrWUmR6mpLu4l1MPBaRAW27qnaQBhLhPkEsdbP8f5-of2-v50Ou_-HP6y1t5puMAqYGMlZ1qNkKZlJGng3XnuANQwnpyYujkIursRuJVqSKz7vkPb6rZJKVXazaJnilOBGQBWcMhKEh5SmeqYZJevsefp_BTH5Tjd8JbR2ygig9kzeoeBxgRI3XEL5DJL16N73M_VaPOHOtlnaqU-1YTLucm0eAAPxNn4_IjjXvjX2J9flWqCPA.F9npSw.cHki2vyLF3_B-3RDXykRakvNdRI",
        "domain": ".lanhuapp.com",
        "path": "/",
        "sameSite": "Lax"
    },
]

storage_json = {

    "origins": [
        {
            "origin": "https://lanhuapp.com",
            "localStorage": [
                {
                    "name": "token",
                    "value": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTY5Mzk5NzAwNSwiZXhwIjoxNzI1NTMzMDA1fQ.eyJpZCI6IjNhYTRkYzcxLTcxYmQtNGM1NC1iNDI0LTcxNTI0NzYxY2FjNSJ9.6kh3YrrGSGFyOWDYJqWtONL5aRWy1-TREP5HDCD0mp8"
                },
            ]
        }]}


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


def add_cookies(page: Page):
    page.context.add_cookies(cookies)


def param():
    parser = argparse.ArgumentParser()
    # parser.add_argument("--p", default="saas", choices=["saas", "ts", "enterprise"])
    parser.add_argument(
        "--e",
        default="online",
        choices=["online", "pre", "test"],
    )
    parser.add_argument("--r", default=None)
    return parser.parse_args()


def get_base_url(env):
    if env == "online" or not env:
        return "https://mastergo.com"


def save_test_info(env=None):
    config = get_ini()
    config["pytest"]["env"] = env
    config["pytest"]["base_url"] = get_base_url(env)
    config.write()
