import pytest
from solution import comparar_numeros


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((5, 2), 'primeiro maior'),
        pytest.param((2, 5), 'segundo maior'),
        pytest.param((3, 3), 'iguais'),
        pytest.param((-1, 4), 'segundo maior'),
        pytest.param((-2, -2), 'iguais'),
    ],
)
def test_comparar_numeros(args, esperado):
    assert comparar_numeros(*args) == esperado

