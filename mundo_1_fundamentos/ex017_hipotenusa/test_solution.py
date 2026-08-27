import pytest

from solution import hipotenusa


@pytest.mark.parametrize(
    "cateto_oposto,cateto_adjacente,esperado",
    [
        (3, 4, 5.0),
        (6, 8, 10.0),
        (5, 12, 13.0),
        (1, 1, 1.4142135623730951),
        (0, 6, 6.0),
    ],
)
def test_hipotenusa(cateto_oposto, cateto_adjacente, esperado):
    assert hipotenusa(cateto_oposto, cateto_adjacente) == pytest.approx(esperado)