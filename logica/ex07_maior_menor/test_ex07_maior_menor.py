from solution_ex07_maior_menor import maior_menor
import pytest


@pytest.mark.parametrize("args,esperado", [
    (([3, 1, 4, 1, 5],), (5, 1)),
    (([],), None),
    (([7],), (7, 7)),
    (([-1, -5, -3],), (-1, -5)),
    (([0, 0],), (0, 0)),
    (([100, 5, 200],), (200, 5)),
])
def test_caso(args, esperado):
    assert maior_menor(*args) == esperado
