import pytest
from solution import soma_multiplos_de_3


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((), 41583),
        pytest.param((1, 10), 18),
        pytest.param((5, 12), 27),
        pytest.param((1, 6), 9),
        pytest.param((3, 3), 3),
    ],
)
def test_soma_multiplos_de_3(args, esperado):
    assert soma_multiplos_de_3(*args) == esperado
