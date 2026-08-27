from solution import maior_menor
import pytest


@pytest.mark.parametrize("args,esperado", [
    ([[3, 1, 4, 1, 5]], (5, 1)),
    ([[-1, 2, -3]], (2, -3)),
    ([[7]], (7, 7)),
    ([[]], None),
    ([[10, 10]], (10, 10))
])
def test_caso(args, esperado):
    assert maior_menor(*args) == esperado
