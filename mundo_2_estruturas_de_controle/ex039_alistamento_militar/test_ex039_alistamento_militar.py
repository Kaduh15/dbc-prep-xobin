import pytest

from solution_ex039_alistamento_militar import situacao_alistamento


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((16,), 'faltam 2 anos'),
        pytest.param((17,), 'faltam 1 ano'),
        pytest.param((18,), 'hora de se alistar'),
        pytest.param((21,), 'ja passou 3 anos'),
        pytest.param((30,), 'ja passou 12 anos'),
        # extremos / borda
        pytest.param((0,), 'faltam 18 anos'),
        pytest.param((1,), 'faltam 17 anos'),
        pytest.param((19,), 'ja passou 1 ano'),
        pytest.param((25,), 'ja passou 7 anos'),
        pytest.param((100,), 'ja passou 82 anos'),
    ],
)
def test_situacao_alistamento(args, esperado):
    assert situacao_alistamento(*args) == esperado
