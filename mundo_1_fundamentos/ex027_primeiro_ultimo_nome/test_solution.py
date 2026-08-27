import pytest

from solution import primeiro_ultimo_nome

@pytest.mark.parametrize(
    "args, expected",
    [(('João Silva',), ('João', 'Silva'))],
)
def test_dois_nomes(args, expected):
    assert primeiro_ultimo_nome(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('Maria Clara Souza',), ('Maria', 'Souza'))],
)
def test_tres_nomes(args, expected):
    assert primeiro_ultimo_nome(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('Ana',), ('Ana', 'Ana'))],
)
def test_nome_unico(args, expected):
    assert primeiro_ultimo_nome(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [(('  Pedro  Henrique  ',), ('Pedro', 'Henrique'))],
)
def test_espacos_extra(args, expected):
    assert primeiro_ultimo_nome(*args) == expected
