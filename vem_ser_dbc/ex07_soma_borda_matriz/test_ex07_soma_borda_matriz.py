from solution_ex07_soma_borda_matriz import soma_borda_matriz
import pytest


@pytest.mark.parametrize("args,esperado", [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), 40),
    (([[5]],), 5),
    (([[1, 2], [3, 4]],), 10),
    (([],), 0),
    (([[]],), 0),
    (([[1, 2, 3, 4]],), 10),
    (([[-1, -2], [-3, -4]],), -10),
])
def test_caso(args, esperado):
    assert soma_borda_matriz(*args) == esperado
