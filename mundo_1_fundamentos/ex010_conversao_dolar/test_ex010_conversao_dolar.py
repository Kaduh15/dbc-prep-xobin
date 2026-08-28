from solution_ex010_conversao_dolar import converter_dolar
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((327, 3.27), 100.0),
    ((100, 5.0), 20.0),
    ((0, 3.27), 0.0),
    ((3.27, 3.27), 1.0),
    ((3.27,), 1.0),
    ((50, 5.0), 10.0),
    ((200, 4.0), 50.0),
    ((1, 2.0), 0.5),
    ],
)
def test_converter_dolar(args, esperado):
    assert converter_dolar(*args) == pytest.approx(esperado)
