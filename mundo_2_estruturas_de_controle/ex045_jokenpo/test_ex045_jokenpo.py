import pytest

from solution_ex045_jokenpo import jokenpo


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
        # empates restantes
        pytest.param(('pedra', 'pedra'), 'empate'),
        pytest.param(('tesoura', 'tesoura'), 'empate'),
    ],
)
def test_jokenpo(args, esperado):
    assert jokenpo(*args) == esperado


@pytest.mark.parametrize(
    "args",
    [('lagarto', 'papel'), ('pedra', 'lagarto'), ('', 'pedra'), ('PAPEL', 'pedra')],
)
def test_jokenpo_entrada_invalida(args):
    with pytest.raises(ValueError):
        jokenpo(*args)
