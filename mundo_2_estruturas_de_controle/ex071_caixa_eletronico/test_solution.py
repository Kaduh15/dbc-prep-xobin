import pytest

from solution import caixa_eletronico


@pytest.mark.parametrize(
    "args, expected",
    [
    ((188,), {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1}),
    ((650,), {100: 6, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}),
    ((30,), {100: 0, 50: 0, 20: 1, 10: 1, 5: 0, 2: 0, 1: 0}),
    ((0,), {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}),
    ],
)
def test_caixa_eletronico(args, expected):
    assert caixa_eletronico(*args) == expected
