import pytest
from solution_ex055_maior_menor_peso import maior_menor_peso


@pytest.mark.parametrize(
    "pesos, esperado",
    [
        ([70.5, 80.0, 55.3, 90.2, 62.1], (90.2, 55.3)),
        ([50.0, 50.0], (50.0, 50.0)),
        ([100.0, 20.0, 40.0], (100.0, 20.0)),
        ([65.0, 65.0, 65.0], (65.0, 65.0)),
        ([42.0], (42.0, 42.0)),
        ([20.0, 100.0, 40.0], (100.0, 20.0)),
        ([0.5, 0.1, 0.9], (0.9, 0.1)),
    ],
)
def test_maior_menor_peso(pesos, esperado):
    assert maior_menor_peso(pesos) == esperado
