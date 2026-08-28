from solution_ex03_anagrama import anagrama
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('listen', 'silent'), True),
    (('triangle', 'integral'), True),
    (('cat', 'dog'), False),
    (('hello', 'hello'), True),
    (('', ''), True),
    (('a', 'b'), False),
    (('anagram', 'nag a ram'), True),
    (('python', 'java'), False),
])
def test_caso(args, esperado):
    assert anagrama(*args) == esperado
