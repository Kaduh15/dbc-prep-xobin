import pytest

from solution import prestacao_mensal, aprova_emprestimo

@pytest.mark.parametrize(
    "args, expected",
    [((100000, 20), 416.6666666666667)],
)
def test_prestacao_mensal_basica(args, expected):
    assert prestacao_mensal(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((30000, 1), 2500.0)],
)
def test_prestacao_mensal_doze_meses(args, expected):
    assert prestacao_mensal(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((240000, 20), 1000.0)],
)
def test_prestacao_mensal_mais_anos(args, expected):
    assert prestacao_mensal(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((100000, 2000, 20), True)],
)
def test_aprova_emprestimo_aprovado(args, expected):
    assert aprova_emprestimo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((200000, 2000, 20), False)],
)
def test_aprova_emprestimo_negado(args, expected):
    assert aprova_emprestimo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((120000, 5000, 10), True)],
)
def test_aprova_emprestimo_salario_alto(args, expected):
    assert aprova_emprestimo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((80000, 1500, 10), False)],
)
def test_aprova_emprestimo_prazo_curto(args, expected):
    assert aprova_emprestimo(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((72000, 2000, 10), True)],
)
def test_aprova_emprestimo_limite_exato(args, expected):
    assert aprova_emprestimo(*args) == expected
