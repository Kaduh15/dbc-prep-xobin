import pytest
from solution import valor_final


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((100, 'dinheiro'), 90.0),
        pytest.param((100, 'cartao_avista'), 95.0),
        pytest.param((100, '2x'), 100.0),
        pytest.param((100, '3x_mais'), 120.0),
        pytest.param((80, 'dinheiro'), 72.0),
    ],
)
def test_valor_final(args, esperado):
    assert valor_final(*args) == esperado


def test_valor_final_entrada_invalida():
    with pytest.raises(ValueError):
        valor_final(100, 'parcelado')

