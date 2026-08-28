from solution_ex009_tabuada import tabuada
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((7,), [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]),
    ((2,), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),
    ((0,), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ((-3,), [-3, -6, -9, -12, -15, -18, -21, -24, -27, -30]),
    ((1,), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ((10,), [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
    ((-1,), [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]),
    ],
)
def test_tabuada(args, esperado):
    assert tabuada(*args) == esperado

def test_tabuada_tamanho():
    assert len(tabuada(5)) == 10
