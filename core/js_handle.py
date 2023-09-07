# -*- coding: utf-8 -*-

"""
@Time : 2022/6/9
@Author : SunShijiang
@File : js_handle.py
@Description : 
"""

import re

from core.utils import home


def open_js(js_name):
    with open(home() + "/js_data/" + js_name, "r", encoding="utf-8") as q:
        js = q.read()
    return js


# 加载 FPS JS 程序
def get_js():
    return open_js("fps-check.js")


# 开始收集 FPS
def start_js():
    return open_js("fps-check-start.js")


# 停止收集 FPS
def end_js():
    return open_js("fps-check-end.js")


#  收集TTi
def tti_js():
    return open_js("tti.js")


# 获取日志内 FPS 相关数据
def get_value(one, two, text):
    r = re.search(one + r'(.*?)' + two, text)
    try:
        if r.groups() is not None:
            return r.groups()
    except TypeError:
        raise


# 筛选日志内 debug 信息（FPS 相关信息输出为 debug 格式日志）
def get_msg(log_path):
    with open(log_path, "r") as q:
        js = q.read()
    for s in js:
        if s['level'] == 'DEBUG':
            return s


if __name__ == "__main__":
    print(start_js())
