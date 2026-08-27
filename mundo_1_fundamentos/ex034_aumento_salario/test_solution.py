import pytest

from solution import novo_salario

@pytest.mark.parametrize(
    "args, expected",
    [((1000,), 1150.0)],
)
def test_quinze(args, expected):
    assert novo_salario(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((1250,), 1437.5)],
)
def test_limite_quinze(args, expected):
    assert novo_salario(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((1250.01,), 1375.01)],
)
def test_acima_limite(args, expected):
    assert novo_salario(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((1500,), 1650.0)],
)
def test_dez(args, expected):
    assert novo_salario(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((800,), 920.0)],
)
def test_baixo(args, expected):
    assert novo_salario(*args) == expected
