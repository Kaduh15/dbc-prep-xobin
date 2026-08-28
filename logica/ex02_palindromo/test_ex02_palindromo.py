from solution_ex02_palindromo import palindromo
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('arara',), True),
    (('A man a plan a canal Panama',), True),
    (('hello',), False),
    (('',), True),
    (('Ana',), True),
    (('12321',), True),
    (('a',), True),
    (('ab',), False),
])
def test_caso(args, esperado):
    assert palindromo(*args) == esperado
