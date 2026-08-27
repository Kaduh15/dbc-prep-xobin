import pytest

from solution import analise_produtos


@pytest.mark.parametrize(
    "args, expected",
    [
    (([('Borracha', 2), ('Caderno', 15), ('Mouse', 120)],), (137.0, 2, "Borracha")),
    (([('X', 100.0)],), (100.0, 0, "X")),
    (([('A', 5), ('B', 3)],), (8.0, 2, "B")),
    (([],), (0.0, 0, "")),
    ],
)
def test_analise_produtos(args, expected):
    assert analise_produtos(*args) == expected
