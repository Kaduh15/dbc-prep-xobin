from solution_ex032_ano_bissexto import eh_bissexto
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((2024,), True),
    ((2023,), False),
    ((2000,), True),
    ((1900,), False),
    ((1600,), True),
    ((4,), True),
    ((1700,), False),
    ((2100,), False),
    ((0,), True),
    ((400,), True),
    ((1996,), True),
    ((1,), False),
    ((100,), False),
    ((700,), False),
])
def test_caso(args, esperado):
    assert eh_bissexto(*args) == esperado
