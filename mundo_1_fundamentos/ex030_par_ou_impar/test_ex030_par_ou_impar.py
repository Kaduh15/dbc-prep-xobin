from solution_ex030_par_ou_impar import par_ou_impar
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((2,), 'PAR'),
    ((3,), 'ÍMPAR'),
    ((0,), 'PAR'),
    ((-4,), 'PAR'),
    ((-7,), 'ÍMPAR'),
    ((1,), 'ÍMPAR'),
    ((-2,), 'PAR'),
    ((-1,), 'ÍMPAR'),
    ((4,), 'PAR'),
    ((100,), 'PAR'),
    ((101,), 'ÍMPAR'),
])
def test_caso(args, esperado):
    assert par_ou_impar(*args) == esperado
