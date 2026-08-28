import pytest

from solution_ex067_tabuada_varios_numeros import tabuada


@pytest.mark.parametrize(
    "args, expected",
    [
    ((7,), [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70]),
    ((5,), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),
    ((-3,), None),
    ((0,), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ((1,), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ((12,), [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120]),
    ((-1,), None),
    ],
)
def test_tabuada(args, expected):
    assert tabuada(*args) == expected
