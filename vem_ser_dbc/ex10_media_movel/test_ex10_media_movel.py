from solution_ex10_media_movel import media_movel
import pytest


@pytest.mark.parametrize("args,esperado", [
    (([1, 2, 3, 4], 2), [1.5, 2.5, 3.5]),
    (([5], 1), [5.0]),
    (([1, 2, 3], 3), [2.0]),
    (([1, 2, 3], 4), []),
    (([], 2), []),
    (([1, 2, 3], 0), []),
    (([1, 2, 3, 4], 3), [2.0, 3.0]),
    (([-1, -2, -3, -4], 2), [-1.5, -2.5, -3.5]),
])
def test_caso(args, esperado):
    assert media_movel(*args) == esperado
