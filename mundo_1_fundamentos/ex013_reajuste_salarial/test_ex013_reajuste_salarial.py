import pytest

from solution_ex013_reajuste_salarial import calcula_aumento


@pytest.mark.parametrize(
    "entrada,esperado",
    [
        (1000, 1150.0),
        (2600, 2990.0),
        (0, 0.0),
        (1250, 1437.5),
        (2000, 2300.0),
        (-100, -115.0),
        (1234.56, 1419.744),
        (1, 1.15),
        (10000, 11500.0),
    ],
)
def test_calcula_aumento(entrada, esperado):
    assert calcula_aumento(entrada) == pytest.approx(esperado)
