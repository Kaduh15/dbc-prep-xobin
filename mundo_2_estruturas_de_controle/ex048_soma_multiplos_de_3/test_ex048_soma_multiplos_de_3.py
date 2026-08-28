import pytest

from solution_ex048_soma_multiplos_de_3 import soma_multiplos_de_3


@pytest.mark.parametrize(
    "args, esperado",
    [
        pytest.param((), 41583),
        pytest.param((1, 10), 18),
        pytest.param((5, 12), 27),
        pytest.param((1, 6), 9),
        pytest.param((3, 3), 3),
        # extremos / borda
        pytest.param((0, 10), 18),    # 0, 3, 6, 9
        pytest.param((10, 15), 27),   # 12, 15
        pytest.param((1, 3), 3),
        pytest.param((100, 100), 0),  # 100 nao e multiplo de 3
    ],
)
def test_soma_multiplos_de_3(args, esperado):
    assert soma_multiplos_de_3(*args) == esperado
