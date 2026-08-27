import pytest

from solution import pa_continua


@pytest.mark.parametrize(
    "args, expected",
    [
    ((2, 3, [5]), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]),
    ((2, 3, []), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]),
    ((2, 3, [3, 0]), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]),
    ((2, 3, [0, 5]), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]),
    ((1, 5, [2]), [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56]),
    ],
)
def test_pa_continua(args, expected):
    assert pa_continua(*args) == expected
