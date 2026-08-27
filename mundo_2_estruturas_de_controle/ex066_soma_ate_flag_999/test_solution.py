import pytest

from solution import numeros_ate_999


@pytest.mark.parametrize(
    "args, expected",
    [
    (([5, 999],), (1, 5)),
    (([7, 8, 999, 10],), (2, 15)),
    (([999],), (0, 0)),
    (([],), (0, 0)),
    ],
)
def test_numeros_ate_999(args, expected):
    assert numeros_ate_999(*args) == expected
