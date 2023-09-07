import pytest

from core.utils import param, save_test_info

if __name__ == '__main__':
    env = param().e
    save_test_info(env)
    cases = "./cases"
    # cases = './cases/test_enter_project.py'

    pytest.main(["./cases/test_enter_project.py"])
