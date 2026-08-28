import pytest

from solution_ex016_porcao_inteira import parte_inteira


@pytest.mark.parametrize(
    "numero,esperado",
    [
        (6.127, 6),
        (100.5, 100),
        (-3.9, -3),
        (7.0, 7),
        (0.999, 0),
        (-0.5, 0),
        (0.0, 0),
        (-2.0, -2),
        (1.9, 1),
        (123.99, 123),
        (-123.99, -123),
    ],
)
def test_parte_inteira(numero, esperado):
    assert parte_inteira(numero) == esperado
