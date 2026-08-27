from solution import fibonacci
import pytest


@pytest.mark.parametrize("args,esperado", [
    ([0], 0),
    ([1], 1),
    ([2], 1),
    ([10], 55),
    ([15], 610)
])
def test_caso(args, esperado):
    assert fibonacci(*args) == esperado
