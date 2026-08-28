import pytest

from solution_ex044_condicao_pagamento import valor_final


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((100, 'dinheiro'), 90.0),
        pytest.param((100, 'cartao_avista'), 95.0),
        pytest.param((100, '2x'), 100.0),
        pytest.param((100, '3x_mais'), 120.0),
        pytest.param((80, 'dinheiro'), 72.0),
        # extremos
        pytest.param((0, 'dinheiro'), 0.0),
        pytest.param((80, 'cartao_avista'), 76.0),
        pytest.param((200, '2x'), 200.0),
        pytest.param((200, '3x_mais'), 240.0),
        pytest.param((50, 'dinheiro'), 45.0),
        pytest.param((10, 'cartao_avista'), 9.5),
    ],
)
def test_valor_final(args, esperado):
    assert valor_final(*args) == esperado


@pytest.mark.parametrize("condicao", ['parcelado', '', 'cheque', 'DINHEIRO'])
def test_valor_final_entrada_invalida(condicao):
    with pytest.raises(ValueError):
        valor_final(100, condicao)
