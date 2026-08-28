import pytest

from solution_ex064_soma_com_flag_999 import soma_ignorando_flag


@pytest.mark.parametrize(
    "args, expected",
    [
    (([2, 5, 999],), (2, 7)),
    (([1, 2, 3, 999],), (3, 6)),
    (([999],), (0, 0)),
    (([],), (0, 0)),
    (([1, 999, 2],), (2, 3)),
    (([999, 1, 999, 2, 999],), (2, 3)),
    (([-5, 999, 10],), (2, 5)),
    (([1, 2, 3],), (3, 6)),
    (([999, 999],), (0, 0)),
    ],
)
def test_soma_ignorando_flag(args, expected):
    assert soma_ignorando_flag(*args) == expected
