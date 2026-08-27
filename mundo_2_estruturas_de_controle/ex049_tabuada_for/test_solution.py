import pytest
from solution import tabuada


@pytest.mark.parametrize(
    "n, esperado",
    [
        (5, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),
        (7, [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]),
        (0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (3, [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]),
        (10, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
    ],
)
def test_tabuada(n, esperado):
    assert tabuada(n) == esperado
