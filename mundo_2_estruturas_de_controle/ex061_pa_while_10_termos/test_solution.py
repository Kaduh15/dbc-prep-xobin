import pytest

from solution import dez_termos_pa


@pytest.mark.parametrize(
    "args, expected",
    [
    ((2, 3), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]),
    ((1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ((10, -2), [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]),
    ],
)
def test_dez_termos_pa(args, expected):
    assert dez_termos_pa(*args) == expected
