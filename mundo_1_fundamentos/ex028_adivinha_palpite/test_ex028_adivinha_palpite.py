from solution_ex028_adivinha_palpite import venceu_adivinhacao
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((3, 3), True),
    ((3, 5), False),
    ((0, 0), True),
    ((5, 0), False),
    ((5, 5), True),
    ((2, 3), False),
    ((0, 5), False),
    ((4, 4), True),
    ((1, 0), False),
    ((-1, -1), True),
])
def test_caso(args, esperado):
    assert venceu_adivinhacao(*args) == esperado
