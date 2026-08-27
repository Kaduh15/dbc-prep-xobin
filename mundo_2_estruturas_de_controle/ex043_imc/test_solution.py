import pytest
from solution import imc


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((50, 1.75), 'Abaixo do Peso'),
        pytest.param((70, 1.75), 'Peso Ideal'),
        pytest.param((90, 1.75), 'Sobrepeso'),
        pytest.param((110, 1.75), 'Obesidade'),
        pytest.param((130, 1.75), 'Obesidade Morbida'),
        pytest.param((60, 1.75), 'Peso Ideal'),
    ],
)
def test_imc(args, esperado):
    assert imc(*args) == esperado

