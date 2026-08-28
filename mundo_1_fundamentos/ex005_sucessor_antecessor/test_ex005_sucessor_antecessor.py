from solution_ex005_sucessor_antecessor import sucessor_antecessor
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((10,), (9, 11)),
    ((0,), (-1, 1)),
    ((-5,), (-6, -4)),
    ((1,), (0, 2)),
    ((2,), (1, 3)),
    ((-1,), (-2, 0)),
    ((100,), (99, 101)),
    ((-100,), (-101, -99)),
    ],
)
def test_sucessor_antecessor(args, esperado):
    assert sucessor_antecessor(*args) == esperado
