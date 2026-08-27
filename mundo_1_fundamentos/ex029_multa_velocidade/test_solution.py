import pytest

from solution import multa_velocidade

@pytest.mark.parametrize(
    "args, expected",
    [((80,), 0.0)],
)
def test_limite(args, expected):
    assert multa_velocidade(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((81,), 7.0)],
)
def test_um_acima(args, expected):
    assert multa_velocidade(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((90,), 70.0)],
)
def test_noventa(args, expected):
    assert multa_velocidade(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((200,), 840.0)],
)
def test_duzentos(args, expected):
    assert multa_velocidade(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((79.9,), 0.0)],
)
def test_abaixo(args, expected):
    assert multa_velocidade(*args) == expected

@pytest.mark.parametrize(
    "args, expected",
    [((-5,), 0.0)],
)
def test_negativo(args, expected):
    assert multa_velocidade(*args) == expected
