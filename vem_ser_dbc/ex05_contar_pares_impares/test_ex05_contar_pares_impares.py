from solution_ex05_contar_pares_impares import contar_pares_impares
import pytest


@pytest.mark.parametrize("args,esperado", [
    (([],), (0, 0)),
    (([1],), (0, 1)),
    (([2],), (1, 0)),
    (([1, 2, 3, 4],), (2, 2)),
    (([0],), (1, 0)),
    (([-2, -3, -4],), (2, 1)),
    (([2, 4, 6],), (3, 0)),
])
def test_caso(args, esperado):
    assert contar_pares_impares(*args) == esperado
