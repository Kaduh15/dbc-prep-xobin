import pytest

from solution import converter_dolar


@pytest.mark.parametrize(
    "reais,cotacao,esperado",
    [
        (327, 3.27, 100.0),
        (100, 5.0, 20.0),
        (0, 3.27, 0.0),
        (3.27, 3.27, 1.0),
    ],
)
def test_converter_dolar(reais, cotacao, esperado):
    assert converter_dolar(reais, cotacao) == pytest.approx(esperado)


def test_converter_dolar_cotacao_padrao():
    assert converter_dolar(3.27) == pytest.approx(1.0)