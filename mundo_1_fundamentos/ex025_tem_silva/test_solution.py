import pytest

from solution import tem_silva

@pytest.mark.parametrize(
    "args, expected",
    [(('João Silva Pereira',), True)],
)
def test_com_silva(args, expected):
    assert tem_silva(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('MARIA DA SILVA',), True)],
)
def test_mais_minusculas(args, expected):
    assert tem_silva(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('Ana Souza',), False)],
)
def test_sem_silva(args, expected):
    assert tem_silva(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('Silvania',), True)],
)
def test_substring(args, expected):
    assert tem_silva(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('',), False)],
)
def test_vazio(args, expected):
    assert tem_silva(*args) == expected
