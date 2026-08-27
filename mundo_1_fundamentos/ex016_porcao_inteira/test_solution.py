import pytest

from solution import parte_inteira


@pytest.mark.parametrize(
    "numero,esperado",
    [
        (6.127, 6),
        (100.5, 100),
        (-3.9, -3),
        (7.0, 7),
        (0.999, 0),
    ],
)
def test_parte_inteira(numero, esperado):
    assert parte_inteira(numero) == esperado