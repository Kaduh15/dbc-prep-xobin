import pytest

from solution import fibonacci


@pytest.mark.parametrize(
    "args, expected",
    [
    ((0,), []),
    ((1,), [0]),
    ((2,), [0, 1]),
    ((5,), [0, 1, 1, 2, 3]),
    ((10,), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ],
)
def test_fibonacci(args, expected):
    assert fibonacci(*args) == expected
