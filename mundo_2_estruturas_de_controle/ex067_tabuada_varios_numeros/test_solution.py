import pytest

from solution import tabuada


@pytest.mark.parametrize(
    "args, expected",
    [
    ((7,), [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70]),
    ((5,), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),
    ((-3,), None),
    ((0,), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ],
)
def test_tabuada(args, expected):
    assert tabuada(*args) == expected
