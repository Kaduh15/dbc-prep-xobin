from solution_ex035_forma_triangulo import forma_triangulo
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((3, 4, 5), True),
    ((1, 2, 3), False),
    ((10, 1, 1), False),
    ((5.5, 5.5, 5.5), True),
    ((7, 2, 4), False),
    ((2, 3, 4), True),
    ((1, 1, 1), True),
    ((2, 2, 4), False),
    ((3, 3, 6), False),
    ((5, 5, 10), False),
    ((1, 1, 2), False),
    ((1, 1, 1.999), True),
    ((0.1, 0.1, 0.1), True),
    ((3, 3, 5.999), True),
])
def test_caso(args, esperado):
    assert forma_triangulo(*args) == esperado
