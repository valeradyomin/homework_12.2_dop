import pytest
from utils.divide_func import divide_nums


@pytest.mark.parametrize("a, b, expected_result", [(50, 2, 25),
                                                   (15, 3, 5),
                                                   (8.4, 2, 4.2)])
def test_divide_nums_good(a, b, expected_result):
    assert divide_nums(a, b) == expected_result


def test_divide_nums_errors():
    with pytest.raises(ZeroDivisionError):
        divide_nums(7, 0)
