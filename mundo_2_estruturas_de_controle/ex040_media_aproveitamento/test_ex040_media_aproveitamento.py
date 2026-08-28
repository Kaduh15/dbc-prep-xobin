import pytest

from solution_ex040_media_aproveitamento import media_aproveitamento


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((4, 4), 'Reprovado'),
        pytest.param((4, 6), 'Recuperacao'),
        pytest.param((5, 8), 'Recuperacao'),
        pytest.param((7, 7), 'Aprovado'),
        pytest.param((8, 10), 'Aprovado'),
        # extremos / borda
        pytest.param((5, 5), 'Recuperacao'),   # media == 5 (limite inferior inclusivo)
        pytest.param((6, 7), 'Recuperacao'),   # media == 6.5
        pytest.param((8, 6), 'Aprovado'),      # media == 7 (limite inclusivo)
        pytest.param((0, 0), 'Reprovado'),     # media == 0
        pytest.param((10, 10), 'Aprovado'),    # media == 10
        pytest.param((3, 6), 'Reprovado'),     # media == 4.5
    ],
)
def test_media_aproveitamento(args, esperado):
    assert media_aproveitamento(*args) == esperado
