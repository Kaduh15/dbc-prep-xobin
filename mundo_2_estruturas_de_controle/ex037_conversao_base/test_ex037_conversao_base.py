import pytest

from solution_ex037_conversao_base import converter_base


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
        # extremos / borda
        pytest.param((0, 1), '0'),
        pytest.param((0, 3), '0'),
        pytest.param((16, 1), '10000'),
        pytest.param((16, 3), '10'),
        pytest.param((31, 1), '11111'),
        pytest.param((8, 2), '10'),
        pytest.param((1000, 3), '3e8'),
    ],
)
def test_converter_base(args, esperado):
    assert converter_base(*args) == esperado


@pytest.mark.parametrize("base", [0, 4, 9, -1])
def test_converter_base_entrada_invalida(base):
    with pytest.raises(ValueError):
        converter_base(10, base)
