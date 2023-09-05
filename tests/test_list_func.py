import pytest

from utils.list_func import app_list


@pytest.fixture
def some_fixt():
    return [1, 2, 3]


@pytest.mark.parametrize("item, expected_result", [(4, [1, 2, 3, 4]),
                                                   (5, [1, 2, 3, 5]),
                                                   ("book", [1, 2, 3, "book"]),
                                                   (None, [1, 2, 3])])
def test_app_list(some_fixt, item, expected_result):
    assert app_list(some_fixt, item) == expected_result
