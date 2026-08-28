import pytest

from solution_ex047_numeros_pares import numeros_pares


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]),
        pytest.param((1, 10), [2, 4, 6, 8, 10]),
        pytest.param((15, 25), [16, 18, 20, 22, 24]),
        pytest.param((3, 3), []),
        pytest.param((2, 8), [2, 4, 6, 8]),
        # extremos / borda
        pytest.param((0, 6), [0, 2, 4, 6]),
        pytest.param((1, 1), []),
        pytest.param((7, 7), []),
        pytest.param((20, 30), [20, 22, 24, 26, 28, 30]),
    ],
)
def test_numeros_pares(args, esperado):
    assert numeros_pares(*args) == esperado
