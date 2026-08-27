import pytest

from solution import calcular_tinta


@pytest.mark.parametrize(
    "largura,altura,esperado",
    [
        (2, 2, (4.0, 2.0)),
        (7, 4, (28.0, 14.0)),
        (0, 5, (0.0, 0.0)),
        (2.5, 4, (10.0, 5.0)),
    ],
)
def test_calcular_tinta(largura, altura, esperado):
    assert calcular_tinta(largura, altura) == esperado