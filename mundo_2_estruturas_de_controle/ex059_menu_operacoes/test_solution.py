import pytest
from solution import aplicar_menu


@pytest.mark.parametrize(
    "valor1, valor2, opcao, esperado",
    [
        (10, 5, 1, 15.0),    # somar
        (10, 5, 2, 50.0),    # multiplicar
        (10, 5, 3, 10.0),    # maior
        (4, 8, 3, 8.0),      # maior
        (10, 5, 5, None),    # sair -> sem operação
        (10, 5, 4, None),    # novos números -> sem operação
    ],
)
def test_aplicar_menu(valor1, valor2, opcao, esperado):
    assert aplicar_menu(valor1, valor2, opcao) == esperado
