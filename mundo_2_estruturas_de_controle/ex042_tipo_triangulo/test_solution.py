import pytest
from solution import tipo_triangulo


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((2, 2, 2), 'equilatero'),
        pytest.param((3, 3, 5), 'isosceles'),
        pytest.param((3, 4, 5), 'escaleno'),
        pytest.param((1, 1, 3), 'invalido'),
        pytest.param((10, 2, 3), 'invalido'),
    ],
)
def test_tipo_triangulo(args, esperado):
    assert tipo_triangulo(*args) == esperado

