from solution_ex11_numero_primo import numero_primo
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((0,), False),
    ((1,), False),
    ((2,), True),
    ((3,), True),
    ((4,), False),
    ((9,), False),
    ((97,), True),
    ((25,), False),
])
def test_caso(args, esperado):
    assert numero_primo(*args) == esperado
