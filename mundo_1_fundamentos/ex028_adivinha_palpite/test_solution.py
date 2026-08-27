import pytest

from solution import venceu_adivinhacao

@pytest.mark.parametrize(
    "args, expected",
    [((3, 3), True)],
)
def test_acertou(args, expected):
    assert venceu_adivinhacao(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((3, 5), False)],
)
def test_errou(args, expected):
    assert venceu_adivinhacao(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((0, 0), True)],
)
def test_zero(args, expected):
    assert venceu_adivinhacao(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((5, 0), False)],
)
def test_diferente_limite(args, expected):
    assert venceu_adivinhacao(*args) == expected
