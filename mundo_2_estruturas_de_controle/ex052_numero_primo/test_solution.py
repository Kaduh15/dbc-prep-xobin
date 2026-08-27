import pytest
from solution import eh_primo


@pytest.mark.parametrize(
    "n, esperado",
    [
        (2, True),
        (3, True),
        (7, True),
        (97, True),
        (1, False),
        (4, False),
        (12, False),
        (100, False),
        (0, False),
    ],
)
def test_eh_primo(n, esperado):
    assert eh_primo(n) == esperado
