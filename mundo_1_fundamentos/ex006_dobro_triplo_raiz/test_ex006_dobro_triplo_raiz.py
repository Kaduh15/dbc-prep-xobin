from solution_ex006_dobro_triplo_raiz import dobro_triplo_raiz
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((9,), (18.0, 27.0, 3.0)),
    ((4,), (8.0, 12.0, 2.0)),
    ((0,), (0.0, 0.0, 0.0)),
    ((2,), (4.0, 6.0, 1.4142135623730951)),
    ((7,), (14.0, 21.0, 2.6457513110645907)),
    ((16,), (32.0, 48.0, 4.0)),
    ((1,), (2.0, 3.0, 1.0)),
    ((0.5,), (1.0, 1.5, 0.7071067811865476)),
    ],
)
def test_dobro_triplo_raiz(args, esperado):
    assert dobro_triplo_raiz(*args) == esperado
