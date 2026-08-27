import pytest

from solution import estatisticas


@pytest.mark.parametrize(
    "args, expected",
    [
    (([7, 5, 8, 3],), (5.75, 8, 3)),
    (([10],), (10.0, 10, 10)),
    (([2, 9, 4],), (5.0, 9, 2)),
    (([5, 5, 5, 5],), (5.0, 5, 5)),
    ],
)
def test_estatisticas(args, expected):
    assert estatisticas(*args) == expected
