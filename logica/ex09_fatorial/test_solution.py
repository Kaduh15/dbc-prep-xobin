from solution import fatorial
import pytest


@pytest.mark.parametrize("args,esperado", [
    ([0], 1),
    ([1], 1),
    ([5], 120),
    ([6], 720),
    ([10], 3628800)
])
def test_caso(args, esperado):
    assert fatorial(*args) == esperado
