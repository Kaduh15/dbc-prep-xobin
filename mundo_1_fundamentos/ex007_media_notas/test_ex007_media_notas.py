from solution_ex007_media_notas import media_notas
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((7, 7), 7.0),
    ((5.5, 8.5), 7.0),
    ((10, 2), 6.0),
    ((0, 0), 0.0),
    ((1, 9), 5.0),
    ((8.5, 7.5), 8.0),
    ((0, 10), 5.0),
    ((6.25, 6.25), 6.25),
    ],
)
def test_media_notas(args, esperado):
    assert media_notas(*args) == esperado
