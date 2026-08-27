import pytest

from solution import tabuada


@pytest.mark.parametrize(
    "n,esperado",
    [
        (7, [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]),
        (2, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),
        (0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (-3, [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30]),
    ],
)
def test_tabuada(n, esperado):
    assert tabuada(n) == esperado
    assert len(tabuada(n)) == 10