import pytest
from solution import jokenpo


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param(('pedra', 'tesoura'), 'usuario'),
        pytest.param(('tesoura', 'papel'), 'usuario'),
        pytest.param(('papel', 'pedra'), 'usuario'),
        pytest.param(('tesoura', 'pedra'), 'computador'),
        pytest.param(('papel', 'tesoura'), 'computador'),
        pytest.param(('pedra', 'papel'), 'computador'),
        pytest.param(('papel', 'papel'), 'empate'),
    ],
)
def test_jokenpo(args, esperado):
    assert jokenpo(*args) == esperado


def test_jokenpo_entrada_invalida():
    with pytest.raises(ValueError):
        jokenpo('lagarto', 'papel')

