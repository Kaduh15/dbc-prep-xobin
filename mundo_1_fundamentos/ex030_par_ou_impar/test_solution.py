import pytest

from solution import par_ou_impar

@pytest.mark.parametrize(
    "args, expected",
    [((2,), 'PAR')],
)
def test_par(args, expected):
    assert par_ou_impar(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((3,), 'ÍMPAR')],
)
def test_impar(args, expected):
    assert par_ou_impar(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((0,), 'PAR')],
)
def test_zero(args, expected):
    assert par_ou_impar(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((-4,), 'PAR')],
)
def test_neg_par(args, expected):
    assert par_ou_impar(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((-7,), 'ÍMPAR')],
)
def test_neg_impar(args, expected):
    assert par_ou_impar(*args) == expected
