import pytest

from solution import analise_pessoas


@pytest.mark.parametrize(
    "args, expected",
    [
    (([(22, 'M'), (15, 'F'), (30, 'M'), (19, 'F')],), (3, 2, 2)),
    (([(18, 'M'), (20, 'F')],), (1, 1, 0)),
    (([(12, 'F')],), (0, 0, 1)),
    (([],), (0, 0, 0)),
    ],
)
def test_analise_pessoas(args, expected):
    assert analise_pessoas(*args) == expected
