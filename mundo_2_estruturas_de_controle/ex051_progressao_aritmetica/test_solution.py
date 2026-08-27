import pytest
from solution import progressao_aritmetica


@pytest.mark.parametrize(
    "primeiro, razao, n, esperado",
    [
        (2, 3, 10, [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]),
        (10, 10, 10, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
        (5, 0, 10, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),
        (1, 2, 5, [1, 3, 5, 7, 9]),
        (7, -2, 3, [7, 5, 3]),
    ],
)
def test_progressao_aritmetica(primeiro, razao, n, esperado):
    assert progressao_aritmetica(primeiro, razao, n) == esperado
