import pytest

from core.utils import param, save_test_info, home

if __name__ == '__main__':
    env = param().e
    save_test_info(env)
    cases = home() + "/cases/mg/"
    cases = home() + '/cases/mg/test_login.py'

    pytest.main([cases,
                 "--alluredir= report/allure-results",
                 "--html=report/html-report.html",
                 "-W ignore::pytest.PytestConfigWarning"])
