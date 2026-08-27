from solution import numero_primo
import pytest


@pytest.mark.parametrize("args,esperado", [
    ([1], False),
    ([2], True),
    ([3], True),
    ([4], False),
    ([17], True),
    ([97], True),
    ([100], False)
])
def test_caso(args, esperado):
    assert numero_primo(*args) == esperado
