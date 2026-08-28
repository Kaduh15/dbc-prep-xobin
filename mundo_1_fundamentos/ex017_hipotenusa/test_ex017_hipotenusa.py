import pytest

from solution_ex017_hipotenusa import hipotenusa


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (3, 4, 5.0),
        (6, 8, 10.0),
        (5, 12, 13.0),
        (1, 1, 1.4142135623730951),
        (0, 6, 6.0),
        (0, 0, 0.0),
        (7, 24, 25.0),
        (20, 21, 29.0),
    ],
)
def test_hipotenusa(a, b, esperado):
    assert hipotenusa(a, b) == pytest.approx(esperado)
