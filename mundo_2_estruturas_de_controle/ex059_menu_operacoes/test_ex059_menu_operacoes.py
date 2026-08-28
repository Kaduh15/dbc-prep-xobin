import pytest
from solution_ex059_menu_operacoes import aplicar_menu


@pytest.mark.parametrize(
    "valor1, valor2, opcao, esperado",
    [
        (10, 5, 1, 15.0),
        (10, 5, 2, 50.0),
        (10, 5, 3, 10.0),
        (4, 8, 3, 8.0),
        (10, 5, 5, None),
        (10, 5, 4, None),
        (10.5, 2.5, 1, 13.0),
        (-5, -3, 3, -3.0),
        (7, 7, 3, 7.0),
        (10, 5, 0, None),
        (10, 5, 6, None),
    ],
)
def test_aplicar_menu(valor1, valor2, opcao, esperado):
    assert aplicar_menu(valor1, valor2, opcao) == esperado
