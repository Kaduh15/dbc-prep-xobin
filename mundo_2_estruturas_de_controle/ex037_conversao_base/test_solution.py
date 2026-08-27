import pytest
from solution import converter_base


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((10, 1), '1010'),
        pytest.param((10, 2), '12'),
        pytest.param((10, 3), 'a'),
        pytest.param((255, 1), '11111111'),
        pytest.param((255, 2), '377'),
        pytest.param((255, 3), 'ff'),
        pytest.param((0, 2), '0'),
    ],
)
def test_converter_base(args, esperado):
    assert converter_base(*args) == esperado


def test_converter_base_entrada_invalida():
    with pytest.raises(ValueError):
        converter_base(10, 9)

