import pytest

from solution_ex036_emprestimo_bancario import prestacao_mensal, aprova_emprestimo


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((100000, 20), 416.6666666666667),
        pytest.param((30000, 1), 2500.0),
        pytest.param((240000, 20), 1000.0),
        pytest.param((12000, 1), 1000.0),
        pytest.param((100, 1), 8.333333333333334),
        pytest.param((0, 5), 0.0),
        pytest.param((600000, 50), 1000.0),
    ],
)
def test_prestacao_mensal(args, esperado):
    assert prestacao_mensal(*args) == esperado


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((100000, 2000, 20), True),
        pytest.param((200000, 2000, 20), False),
        pytest.param((120000, 5000, 10), True),
        pytest.param((80000, 1500, 10), False),
        pytest.param((72000, 2000, 10), True),   # limite exato: prestacao == 30% do salario
        pytest.param((30000, 2000, 5), True),    # prestacao (500) < 30% (600)
        pytest.param((60000, 2000, 5), False),   # prestacao (1000) > 30% (600)
        pytest.param((72001, 2000, 10), False),  # ligeiramente acima do limite
        pytest.param((1000, 0, 10), False),      # salario zero
    ],
)
def test_aprova_emprestimo(args, esperado):
    assert aprova_emprestimo(*args) == esperado
