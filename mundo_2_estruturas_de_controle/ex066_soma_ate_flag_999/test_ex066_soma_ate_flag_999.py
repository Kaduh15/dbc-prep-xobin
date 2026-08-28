import pytest

from solution_ex066_soma_ate_flag_999 import numeros_ate_999


@pytest.mark.parametrize(
    "args, expected",
    [
    (([5, 999],), (1, 5)),
    (([7, 8, 999, 10],), (2, 15)),
    (([999],), (0, 0)),
    (([],), (0, 0)),
    (([1, 999],), (1, 1)),
    (([1, 2, 999, 4, 999],), (2, 3)),
    (([1, 2, 3],), (3, 6)),
    (([999, 10],), (0, 0)),
    ],
)
def test_numeros_ate_999(args, expected):
    assert numeros_ate_999(*args) == expected
