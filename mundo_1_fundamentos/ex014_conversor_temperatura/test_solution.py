import pytest

from solution import celsius_para_fahrenheit


@pytest.mark.parametrize(
    "celsius,esperado",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
        (25, 77.0),
    ],
)
def test_celsius_para_fahrenheit(celsius, esperado):
    assert celsius_para_fahrenheit(celsius) == pytest.approx(esperado)