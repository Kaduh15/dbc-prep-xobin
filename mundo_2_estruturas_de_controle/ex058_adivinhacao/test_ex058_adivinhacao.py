import pytest
from solution_ex058_adivinhacao import palpites_para_acertar


@pytest.mark.parametrize(
    "numero, tentativas, esperado",
    [
        (5, [8, 2, 5, 9], 3),
        (3, [1, 2, 3], 3),
        (7, [7], 1),
        (9, [1, 2, 3], 3),
        (4, [4, 4], 1),
        (4, [], 0),
        (3, [1], 1),
        (4, [1, 2, 3, 4], 4),
    ],
)
def test_palpites_para_acertar(numero, tentativas, esperado):
    assert palpites_para_acertar(numero, tentativas) == esperado
