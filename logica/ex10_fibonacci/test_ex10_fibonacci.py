from solution_ex10_fibonacci import fibonacci
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((0,), 0),
    ((1,), 1),
    ((2,), 1),
    ((5,), 5),
    ((10,), 55),
    ((6,), 8),
])
def test_caso(args, esperado):
    assert fibonacci(*args) == esperado
