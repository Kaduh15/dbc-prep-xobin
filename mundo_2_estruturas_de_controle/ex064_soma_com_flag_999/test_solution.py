import pytest

from solution import soma_ignorando_flag


@pytest.mark.parametrize(
    "args, expected",
    [
    (([2, 5, 999],), (2, 7)),
    (([1, 2, 3, 999],), (3, 6)),
    (([999],), (0, 0)),
    (([],), (0, 0)),
    ],
)
def test_soma_ignorando_flag(args, expected):
    assert soma_ignorando_flag(*args) == expected
