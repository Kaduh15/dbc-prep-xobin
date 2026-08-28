import pytest

from solution_ex068_par_ou_impar import par_ou_impar


@pytest.mark.parametrize(
    "args, expected",
    [
    ((4, 2, 'par'), True),
    ((5, 4, 'impar'), True),
    ((4, 2, 'impar'), False),
    ((3, 4, 'par'), False),
    ((7, 3, 'par'), True),
    ((7, 3, 'PAR'), True),
    ((5, 5, 'impar'), False),
    ((0, 0, 'par'), True),
    ((1, 2, 'impar'), True),
    ((2, 4, 'impar'), False),
    ((3, 4, 'IMPAR'), True),
    ],
)
def test_par_ou_impar(args, expected):
    assert par_ou_impar(*args) == expected
