from solution_ex011_tinta_parede import calcular_tinta
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((2, 2), (4.0, 2.0)),
    ((7, 4), (28.0, 14.0)),
    ((0, 5), (0.0, 0.0)),
    ((2.5, 4), (10.0, 5.0)),
    ((3, 3), (9.0, 4.5)),
    ((4, 2.5), (10.0, 5.0)),
    ((0.5, 0.5), (0.25, 0.125)),
    ],
)
def test_calcular_tinta(args, esperado):
    assert calcular_tinta(*args) == esperado
