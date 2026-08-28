from solution_ex034_aumento_salario import novo_salario
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((1000,), 1150.0),
    ((1250,), 1437.5),
    ((1250.01,), 1375.01),
    ((1500,), 1650.0),
    ((800,), 920.0),
    ((0,), 0.0),
    ((2000,), 2200.0),
    ((10000,), 11000.0),
    ((10,), 11.5),
])
def test_caso(args, esperado):
    assert novo_salario(*args) == esperado
