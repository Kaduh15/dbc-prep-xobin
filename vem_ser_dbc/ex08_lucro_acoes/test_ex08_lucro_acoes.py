from solution_ex08_lucro_acoes import lucro_acoes
import pytest


@pytest.mark.parametrize("args,esperado", [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
    (([],), 0),
    (([5],), 0),
    (([1, 2, 3, 4, 5],), 4),
    (([3, 3, 3],), 0),
    (([2, 10],), 8),
    (([10, 1],), 0),
])
def test_caso(args, esperado):
    assert lucro_acoes(*args) == esperado
