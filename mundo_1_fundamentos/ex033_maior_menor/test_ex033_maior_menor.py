from solution_ex033_maior_menor import maior_e_menor
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((3, 7, 5), (7, 3)),
    ((1, 2, 3), (3, 1)),
    ((9, 5, 1), (9, 1)),
    ((-1, -5, -2), (-1, -5)),
    ((9, 9, 9), (9, 9)),
    ((5, 5, 3), (5, 3)),
    ((3, 5, 5), (5, 3)),
    ((5, 3, 5), (5, 3)),
    ((1, 1, 1), (1, 1)),
    ((0, 0, 7), (7, 0)),
    ((7, 5, 7), (7, 5)),
    ((-3, -3, -1), (-1, -3)),
])
def test_caso(args, esperado):
    assert maior_e_menor(*args) == esperado
