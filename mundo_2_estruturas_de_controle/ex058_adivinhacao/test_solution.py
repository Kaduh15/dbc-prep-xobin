import pytest
from solution import palpites_para_acertar


@pytest.mark.parametrize(
    "numero, tentativas, esperado",
    [
        (5, [8, 2, 5, 9], 3),   # acerta no 3º palpite
        (3, [1, 2, 3], 3),      # acerta no último
        (7, [7], 1),            # acerta de primeira
        (9, [1, 2, 3], 3),      # nunca acerta -> usa todas as tentativas
        (4, [4, 4], 1),         # acerta no 1º
    ],
)
def test_palpites_para_acertar(numero, tentativas, esperado):
    assert palpites_para_acertar(numero, tentativas) == esperado
