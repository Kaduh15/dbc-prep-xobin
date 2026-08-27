import pytest

from solution import preco_com_desconto


@pytest.mark.parametrize(
    "preco,desconto,esperado",
    [
        (100, 0.05, 95.0),
        (80, 0.05, 76.0),
        (100, 0.10, 90.0),
        (0, 0.05, 0.0),
    ],
)
def test_preco_com_desconto(preco, desconto, esperado):
    assert preco_com_desconto(preco, desconto) == esperado


def test_preco_com_desconto_padrao():
    assert preco_com_desconto(100) == 95.0