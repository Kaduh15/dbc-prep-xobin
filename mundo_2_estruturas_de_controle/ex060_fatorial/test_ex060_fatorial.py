import pytest
from solution_ex060_fatorial import fatorial


@pytest.mark.parametrize(
    "n, esperado",
    [
        (5, 120),
        (0, 1),
        (1, 1),
        (3, 6),
        (10, 3628800),
        (6, 720),
        (2, 2),
        (4, 24),
        (7, 5040),
        (12, 479001600),
    ],
)
def test_fatorial(n, esperado):
    assert fatorial(n) == esperado
