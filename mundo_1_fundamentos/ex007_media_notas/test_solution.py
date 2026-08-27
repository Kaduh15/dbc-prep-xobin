import pytest

from solution import media_notas


@pytest.mark.parametrize(
    "n1,n2,esperado",
    [
        (7, 7, 7.0),
        (5.5, 8.5, 7.0),
        (10, 2, 6.0),
        (0, 0, 0.0),
    ],
)
def test_media_notas(n1, n2, esperado):
    assert media_notas(n1, n2) == esperado