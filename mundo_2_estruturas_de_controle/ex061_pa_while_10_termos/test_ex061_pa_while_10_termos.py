import pytest

from solution_ex061_pa_while_10_termos import dez_termos_pa


@pytest.mark.parametrize(
    "args, expected",
    [
    ((2, 3), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]),
    ((1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ((10, -2), [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]),
    ((5, 0), [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),
    ((0, 4), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]),
    ((-3, -1), [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]),
    ((7, 2), [7, 9, 11, 13, 15, 17, 19, 21, 23, 25]),
    ],
)
def test_dez_termos_pa(args, expected):
    assert dez_termos_pa(*args) == expected
