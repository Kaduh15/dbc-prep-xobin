from solution_ex09_fatorial import fatorial
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((0,), 1),
    ((1,), 1),
    ((5,), 120),
    ((3,), 6),
    ((2,), 2),
    ((6,), 720),
])
def test_caso(args, esperado):
    assert fatorial(*args) == esperado
