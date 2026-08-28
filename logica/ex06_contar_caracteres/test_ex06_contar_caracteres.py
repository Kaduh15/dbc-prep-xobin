from solution_ex06_contar_caracteres import contar_caracteres
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('banana',), {'b': 1, 'a': 3, 'n': 2}),
    (('',), {}),
    (('a',), {'a': 1}),
    (('ab a',), {'a': 2, 'b': 1, ' ': 1}),
    (('aba',), {'a': 2, 'b': 1}),
])
def test_caso(args, esperado):
    assert contar_caracteres(*args) == esperado
