import pytest

from solution_ex015_aluguel_carro import custo_aluguel


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (8, 720, 588.0),
        (5, 100, 315.0),
        (1, 0, 60.0),
        (0, 0, 0.0),
        (2, 50.5, 127.575),
        (2, 50.5, 127.575),
        (0, 1, 0.15),
        (1, 1, 60.15),
        (3, 0.1, 180.015),
        (10, 1000, 750.0),
    ],
)
def test_custo_aluguel(a, b, esperado):
    assert custo_aluguel(a, b) == pytest.approx(esperado)
