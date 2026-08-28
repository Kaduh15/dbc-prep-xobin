import pytest

from solution_ex014_conversor_temperatura import celsius_para_fahrenheit


@pytest.mark.parametrize(
    "entrada,esperado",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
        (25, 77.0),
        (-273.15, -459.67),
        (1, 33.8),
        (-10, 14.0),
        (50, 122.0),
    ],
)
def test_celsius_para_fahrenheit(entrada, esperado):
    assert celsius_para_fahrenheit(entrada) == pytest.approx(esperado)
