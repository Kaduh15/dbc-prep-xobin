import pytest
from solution import soma_pares


@pytest.mark.parametrize(
    "numeros, esperado",
    [
        ([1, 2, 3, 4, 5, 6], 12),
        ([2, 4, 6], 12),
        ([1, 3, 5], 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30),
        ([], 0),
        ([-2, 3, 4, -6], -4),
    ],
)
def test_soma_pares(numeros, esperado):
    assert soma_pares(numeros) == esperado
