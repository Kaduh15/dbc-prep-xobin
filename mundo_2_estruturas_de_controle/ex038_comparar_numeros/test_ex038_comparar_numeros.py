import pytest

from solution_ex038_comparar_numeros import comparar_numeros


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((5, 2), 'primeiro maior'),
        pytest.param((2, 5), 'segundo maior'),
        pytest.param((3, 3), 'iguais'),
        pytest.param((-1, 4), 'segundo maior'),
        pytest.param((-2, -2), 'iguais'),
        # extremos / borda
        pytest.param((0, 0), 'iguais'),
        pytest.param((-3, -7), 'primeiro maior'),
        pytest.param((5, -10), 'primeiro maior'),
        pytest.param((0, -1), 'primeiro maior'),
        pytest.param((-10, -20), 'primeiro maior'),
    ],
)
def test_comparar_numeros(args, esperado):
    assert comparar_numeros(*args) == esperado
