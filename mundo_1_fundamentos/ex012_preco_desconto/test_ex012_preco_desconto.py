from solution_ex012_preco_desconto import preco_com_desconto
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((100, 0.05), 95.0),
    ((80, 0.05), 76.0),
    ((100, 0.10), 90.0),
    ((0, 0.05), 0.0),
    ((100,), 95.0),
    ((200, 0.05), 190.0),
    ((50, 0.10), 45.0),
    ((100, 0.00), 100.0),
    ((1, 1.0), 0.0),
    ((1, 0.5), 0.5),
    ],
)
def test_preco_com_desconto(args, esperado):
    assert preco_com_desconto(*args) == pytest.approx(esperado)
