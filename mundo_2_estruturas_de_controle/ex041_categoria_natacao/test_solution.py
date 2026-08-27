import pytest
from solution import categoria_natacao


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((9,), 'Mirim'),
        pytest.param((14,), 'Infantil'),
        pytest.param((17,), 'Junior'),
        pytest.param((19,), 'Junior'),
        pytest.param((20,), 'Senior'),
        pytest.param((25,), 'Master'),
    ],
)
def test_categoria_natacao(args, esperado):
    assert categoria_natacao(*args) == esperado

