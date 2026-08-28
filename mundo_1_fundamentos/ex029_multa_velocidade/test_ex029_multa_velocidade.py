from solution_ex029_multa_velocidade import multa_velocidade
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((80,), 0.0),
    ((81,), 7.0),
    ((90,), 70.0),
    ((200,), 840.0),
    ((79.9,), 0.0),
    ((-5,), 0.0),
    ((0,), 0.0),
    ((81.5,), 10.5),
    ((80.5,), 3.5),
    ((100,), 140.0),
    ((79,), 0.0),
])
def test_caso(args, esperado):
    assert multa_velocidade(*args) == esperado
