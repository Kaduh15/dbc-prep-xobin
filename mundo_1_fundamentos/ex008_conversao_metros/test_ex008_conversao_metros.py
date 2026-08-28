from solution_ex008_conversao_metros import converter_metros
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((1,), (100.0, 1000.0)),
    ((2.5,), (250.0, 2500.0)),
    ((0,), (0.0, 0.0)),
    ((0.5,), (50.0, 500.0)),
    ((0.25,), (25.0, 250.0)),
    ((10,), (1000.0, 10000.0)),
    ((1.5,), (150.0, 1500.0)),
    ],
)
def test_converter_metros(args, esperado):
    assert converter_metros(*args) == esperado
