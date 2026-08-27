import pytest
from solution import fatorial


@pytest.mark.parametrize(
    "n, esperado",
    [
        (5, 120),
        (0, 1),
        (1, 1),
        (3, 6),
        (10, 3628800),
        (6, 720),
    ],
)
def test_fatorial(n, esperado):
    assert fatorial(n) == esperado
