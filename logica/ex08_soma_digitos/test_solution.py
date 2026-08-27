from solution import soma_digitos
import pytest


@pytest.mark.parametrize("args,esperado", [
    ([123], 6),
    ([0], 0),
    ([5], 5),
    ([-123], 6),
    ([999], 27),
    ([1024], 7)
])
def test_caso(args, esperado):
    assert soma_digitos(*args) == esperado
