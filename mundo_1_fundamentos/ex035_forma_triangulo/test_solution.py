import pytest

from solution import forma_triangulo

@pytest.mark.parametrize(
    "args, expected",
    [((3, 4, 5), True)],
)
def test_valido(args, expected):
    assert forma_triangulo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((1, 2, 3), False)],
)
def test_degenerado(args, expected):
    assert forma_triangulo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((10, 1, 1), False)],
)
def test_lado_grande(args, expected):
    assert forma_triangulo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((5.5, 5.5, 5.5), True)],
)
def test_equilatero(args, expected):
    assert forma_triangulo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((7, 2, 4), False)],
)
def test_impossivel(args, expected):
    assert forma_triangulo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((2, 3, 4), True)],
)
def test_limite(args, expected):
    assert forma_triangulo(*args) == expected
