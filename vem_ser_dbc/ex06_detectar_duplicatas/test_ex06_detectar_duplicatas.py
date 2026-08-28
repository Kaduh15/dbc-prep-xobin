from solution_ex06_detectar_duplicatas import detectar_duplicatas
import pytest


@pytest.mark.parametrize("args,esperado", [
    (([],), False),
    (([1],), False),
    (([1, 2, 3],), False),
    (([1, 1],), True),
    (([1, 2, 3, 2],), True),
    (([0, -1, 0],), True),
])
def test_caso(args, esperado):
    assert detectar_duplicatas(*args) == esperado
