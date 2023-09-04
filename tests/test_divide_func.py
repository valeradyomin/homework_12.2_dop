import pytest
from utils.divide_func import divide_nums


@pytest.mark.parametrize("a, b, expected_result", [(50, 2, 25),
                                                   (15, 3, 5),
                                                   (8.4, 2, 4.2)])
def test_divide_nums_good(a, b, expected_result):
    assert divide_nums(a, b) == expected_result


@pytest.mark.parametrize("exception, number, zero", [(ZeroDivisionError, 7, 0),
                                                     (TypeError, "32", 0)])
def test_divide_nums_errors(exception, number, zero):
    with pytest.raises(exception):
        divide_nums(number, zero)
