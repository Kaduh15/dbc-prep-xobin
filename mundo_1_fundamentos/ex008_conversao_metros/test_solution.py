import pytest

from solution import converter_metros


@pytest.mark.parametrize(
    "metros,esperado",
    [
        (1, (100.0, 1000.0)),
        (2.5, (250.0, 2500.0)),
        (0, (0.0, 0.0)),
        (0.5, (50.0, 500.0)),
    ],
)
def test_converter_metros(metros, esperado):
    assert converter_metros(metros) == esperado