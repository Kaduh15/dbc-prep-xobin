import pytest
from solution import contagem_regressiva


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
        pytest.param((3,), [3, 2, 1, 0]),
        pytest.param((0,), [0]),
    ],
)
def test_contagem_regressiva(args, esperado):
    assert contagem_regressiva(*args) == esperado

