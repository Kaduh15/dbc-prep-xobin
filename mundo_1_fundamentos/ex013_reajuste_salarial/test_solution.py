import pytest

from solution import calcula_aumento


@pytest.mark.parametrize(
    "salario,esperado",
    [
        (1000, 1150.0),
        (2600, 2990.0),
        (0, 0.0),
        (1250, 1437.5),
        (2000, 2300.0),
    ],
)
def test_calcula_aumento(salario, esperado):
    assert calcula_aumento(salario) == pytest.approx(esperado)