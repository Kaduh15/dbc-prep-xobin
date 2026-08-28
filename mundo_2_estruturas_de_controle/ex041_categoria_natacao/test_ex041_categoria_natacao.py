import pytest

from solution_ex041_categoria_natacao import categoria_natacao


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((9,), 'Mirim'),
        pytest.param((14,), 'Infantil'),
        pytest.param((17,), 'Junior'),
        pytest.param((19,), 'Junior'),
        pytest.param((20,), 'Senior'),
        pytest.param((25,), 'Master'),
        # extremos / borda
        pytest.param((0,), 'Mirim'),
        pytest.param((5,), 'Mirim'),
        pytest.param((8,), 'Mirim'),
        pytest.param((10,), 'Infantil'),
        pytest.param((15,), 'Junior'),
        pytest.param((21,), 'Master'),
        pytest.param((30,), 'Master'),
    ],
)
def test_categoria_natacao(args, esperado):
    assert categoria_natacao(*args) == esperado
