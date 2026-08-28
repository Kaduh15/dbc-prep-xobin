from solution_ex01_validar_sudoku_4x4 import validar_sudoku_4x4
import pytest


@pytest.mark.parametrize("args,esperado", [
    (([[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],), True),
    (([[1, 1, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 2], [1, 2, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 5], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3, 4], [3, 4, 1, 0], [2, 1, 4, 3], [4, 3, 2, 1]],), False),
    (([[1, 2, 3], [3, 4, 1], [2, 1, 4]],), False),
    (([],), False),
])
def test_caso(args, esperado):
    assert validar_sudoku_4x4(*args) == esperado
