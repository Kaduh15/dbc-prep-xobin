import pytest

from solution import par_ou_impar


@pytest.mark.parametrize(
    "args, expected",
    [
    ((4, 2, 'par'), True),
    ((5, 4, 'impar'), True),
    ((4, 2, 'impar'), False),
    ((3, 4, 'par'), False),
    ((7, 3, 'par'), True),
    ],
)
def test_par_ou_impar(args, expected):
    assert par_ou_impar(*args) == expected
