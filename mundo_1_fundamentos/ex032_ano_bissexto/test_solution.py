import pytest

from solution import eh_bissexto

@pytest.mark.parametrize(
    "args, expected",
    [((2024,), True)],
)
def test_ano_2024(args, expected):
    assert eh_bissexto(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((2023,), False)],
)
def test_ano_2023(args, expected):
    assert eh_bissexto(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((2000,), True)],
)
def test_ano_2000(args, expected):
    assert eh_bissexto(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((1900,), False)],
)
def test_ano_1900(args, expected):
    assert eh_bissexto(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((1600,), True)],
)
def test_ano_1600(args, expected):
    assert eh_bissexto(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((4,), True)],
)
def test_quatro(args, expected):
    assert eh_bissexto(*args) == expected
