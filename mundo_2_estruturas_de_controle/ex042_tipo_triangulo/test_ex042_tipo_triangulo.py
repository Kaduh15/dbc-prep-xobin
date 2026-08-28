import pytest

from solution_ex042_tipo_triangulo import tipo_triangulo


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((2, 2, 2), 'equilatero'),
        pytest.param((3, 3, 5), 'isosceles'),
        pytest.param((3, 4, 5), 'escaleno'),
        pytest.param((1, 1, 3), 'invalido'),
        pytest.param((10, 2, 3), 'invalido'),
        # extremos / borda
        pytest.param((3, 3, 3), 'equilatero'),
        pytest.param((2, 2, 1), 'isosceles'),
        pytest.param((7, 4, 4), 'isosceles'),
        pytest.param((5, 4, 3), 'escaleno'),
        pytest.param((2, 3, 5), 'invalido'),   # degnerado: 2+3 == 5
        pytest.param((1, 2, 3), 'invalido'),
        pytest.param((1, 1, 2), 'invalido'),
    ],
)
def test_tipo_triangulo(args, esperado):
    assert tipo_triangulo(*args) == esperado
