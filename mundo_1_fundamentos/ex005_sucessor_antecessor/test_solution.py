import pytest

from solution import sucessor_antecessor


@pytest.mark.parametrize(
    "n,esperado",
    [
        (10, (9, 11)),
        (0, (-1, 1)),
        (-5, (-6, -4)),
        (1, (0, 2)),
    ],
)
def test_sucessor_antecessor(n, esperado):
    assert sucessor_antecessor(n) == esperado