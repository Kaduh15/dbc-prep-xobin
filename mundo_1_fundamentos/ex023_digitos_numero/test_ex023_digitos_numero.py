import pytest

from solution_ex023_digitos_numero import decompor_numero


@pytest.mark.parametrize(
    "numero,esperado",
    [
        (1834, (4, 3, 8, 1)),
        (5, (5, 0, 0, 0)),
        (2764, (4, 6, 7, 2)),
        (0, (0, 0, 0, 0)),
        (100, (0, 0, 1, 0)),
        (9999, (9, 9, 9, 9)),
        (10, (0, 1, 0, 0)),
        (1000, (0, 0, 0, 1)),
        (1234, (4, 3, 2, 1)),
    ],
)
def test_decompor_numero(numero, esperado):
    assert decompor_numero(numero) == esperado
