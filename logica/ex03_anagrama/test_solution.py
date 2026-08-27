from solution import anagrama
import pytest


@pytest.mark.parametrize("args,esperado", [
    (['listen', 'silent'], True),
    (['ana', 'naa'], True),
    (['hello', 'world'], False),
    (['', ''], True),
    (['aabb', 'abab'], True),
    (['abc', 'abcd'], False)
])
def test_caso(args, esperado):
    assert anagrama(*args) == esperado
