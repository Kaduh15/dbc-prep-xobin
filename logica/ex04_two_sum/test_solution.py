from solution import two_sum
import pytest


@pytest.mark.parametrize("args,esperado", [
    ([[2, 7, 11, 15], 9], [0, 1]),
    ([[3, 2, 4], 6], [1, 2]),
    ([[3, 3], 6], [0, 1]),
    ([[], 5], None),
    ([[1, 2, 3], 99], None)
])
def test_caso(args, esperado):
    assert two_sum(*args) == esperado
