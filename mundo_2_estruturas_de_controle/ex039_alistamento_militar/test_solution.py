import pytest
from solution import situacao_alistamento


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((16,), 'faltam 2 anos'),
        pytest.param((17,), 'faltam 1 ano'),
        pytest.param((18,), 'hora de se alistar'),
        pytest.param((21,), 'ja passou 3 anos'),
        pytest.param((30,), 'ja passou 12 anos'),
    ],
)
def test_situacao_alistamento(args, esperado):
    assert situacao_alistamento(*args) == esperado

