import pytest

from solution import somar


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (2, 5, 7.0),
        (-3, 8, 5.0),
        (1.5, 2.5, 4.0),
        (0, 0, 0.0),
    ],
)
def test_somar(a, b, esperado):
    assert somar(a, b) == esperado