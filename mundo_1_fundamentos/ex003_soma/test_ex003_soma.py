from solution_ex003_soma import somar
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((2, 5), 7.0),
    ((-3, 8), 5.0),
    ((1.5, 2.5), 4.0),
    ((0, 0), 0.0),
    ((-4, -6), -10.0),
    ((0, 5), 5.0),
    ((-1.25, 2.75), 1.5),
    ((10, 0), 10.0),
    ],
)
def test_somar(args, esperado):
    assert somar(*args) == esperado
