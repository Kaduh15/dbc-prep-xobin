from solution_ex031_preco_passagem import preco_passagem
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((50,), 25.0),
    ((200,), 100.0),
    ((201,), 90.45),
    ((500,), 225.0),
    ((0,), 0.0),
    ((199.9,), 99.95),
    ((1000,), 450.0),
    ((199,), 99.5),
    ((1,), 0.5),
    ((250,), 112.5),
])
def test_caso(args, esperado):
    assert preco_passagem(*args) == esperado
