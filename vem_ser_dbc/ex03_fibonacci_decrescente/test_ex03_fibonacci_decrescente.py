from solution_ex03_fibonacci_decrescente import fibonacci_decrescente
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((1,), [0]),
    ((2,), [1, 0]),
    ((3,), [2, 1, 0]),
    ((6,), [5, 3, 2, 1, 0]),
    ((0,), []),
    ((-5,), []),
    ((10,), [8, 5, 3, 2, 1, 0]),
])
def test_caso(args, esperado):
    assert fibonacci_decrescente(*args) == esperado
