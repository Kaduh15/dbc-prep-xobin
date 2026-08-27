import pytest

from solution import preco_passagem

@pytest.mark.parametrize(
    "args, expected",
    [((50,), 25.0)],
)
def test_ate_200(args, expected):
    assert preco_passagem(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((200,), 100.0)],
)
def test_limite_200(args, expected):
    assert preco_passagem(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((201,), 90.45)],
)
def test_pouco_acima(args, expected):
    assert preco_passagem(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((500,), 225.0)],
)
def test_longa(args, expected):
    assert preco_passagem(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((0,), 0.0)],
)
def test_zero(args, expected):
    assert preco_passagem(*args) == expected
