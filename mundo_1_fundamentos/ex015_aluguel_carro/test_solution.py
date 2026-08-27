import pytest

from solution import custo_aluguel


@pytest.mark.parametrize(
    "dias,km,esperado",
    [
        (8, 720, 588.0),
        (5, 100, 315.0),
        (1, 0, 60.0),
        (0, 0, 0.0),
        (2, 50.5, 127.575),
    ],
)
def test_custo_aluguel(dias, km, esperado):
    assert custo_aluguel(dias, km) == pytest.approx(esperado)