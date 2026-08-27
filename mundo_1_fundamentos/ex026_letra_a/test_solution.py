import pytest

from solution import analisar_letra_a

@pytest.mark.parametrize(
    "args, expected",
    [(('Arara Azul',), (4, 0, 6))],
)
def test_basico(args, expected):
    assert analisar_letra_a(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('Mariana',), (3, 1, 6))],
)
def test_nome(args, expected):
    assert analisar_letra_a(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('xyz',), (0, -1, -1))],
)
def test_sem_a(args, expected):
    assert analisar_letra_a(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('',), (0, -1, -1))],
)
def test_vazio(args, expected):
    assert analisar_letra_a(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('AaA',), (3, 0, 2))],
)
def test_so_a(args, expected):
    assert analisar_letra_a(*args) == expected
