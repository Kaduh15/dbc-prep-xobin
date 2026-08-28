from solution_ex04_frequencia_ignorando_primeira import frequencia_ignorando_primeira
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('',), {}),
    (('abc',), {}),
    (('aab',), {'a': 1}),
    (('aaaa',), {'a': 3}),
    (('banana',), {'a': 2, 'n': 1}),
    (('aa bb',), {'a': 1, 'b': 1}),
])
def test_caso(args, esperado):
    assert frequencia_ignorando_primeira(*args) == esperado
