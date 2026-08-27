import pytest
from solution import media_aproveitamento


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((4, 4), 'Reprovado'),
        pytest.param((4, 6), 'Recuperacao'),
        pytest.param((5, 8), 'Recuperacao'),
        pytest.param((7, 7), 'Aprovado'),
        pytest.param((8, 10), 'Aprovado'),
    ],
)
def test_media_aproveitamento(args, esperado):
    assert media_aproveitamento(*args) == esperado

