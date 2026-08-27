import pytest

from solution import maior_e_menor

@pytest.mark.parametrize(
    "args, expected",
    [((3, 7, 5), (7, 3))],
)
def test_ordem_mista(args, expected):
    assert maior_e_menor(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((1, 2, 3), (3, 1))],
)
def test_crescente(args, expected):
    assert maior_e_menor(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((9, 5, 1), (9, 1))],
)
def test_decrescente(args, expected):
    assert maior_e_menor(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((-1, -5, -2), (-1, -5))],
)
def test_negativos(args, expected):
    assert maior_e_menor(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((9, 9, 9), (9, 9))],
)
def test_iguais(args, expected):
    assert maior_e_menor(*args) == expected
