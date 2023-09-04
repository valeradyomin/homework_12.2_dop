import pytest

from utils.list_func import app_list


@pytest.fixture
def some_fixt():
    return [1, 2, 3]


def test_app_list(some_fixt):
    assert app_list(some_fixt, "book") == [1, 2, 3, "book"]
