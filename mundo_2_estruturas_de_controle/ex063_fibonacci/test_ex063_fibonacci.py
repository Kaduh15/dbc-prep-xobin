import pytest

from solution_ex063_fibonacci import fibonacci


@pytest.mark.parametrize(
    "args, expected",
    [
    ((0,), []),
    ((1,), [0]),
    ((2,), [0, 1]),
    ((5,), [0, 1, 1, 2, 3]),
    ((10,), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ((6,), [0, 1, 1, 2, 3, 5]),
    ((7,), [0, 1, 1, 2, 3, 5, 8]),
    ((-3,), []),
    ],
)
def test_fibonacci(args, expected):
    assert fibonacci(*args) == expected
