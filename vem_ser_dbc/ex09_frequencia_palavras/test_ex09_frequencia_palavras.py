from solution_ex09_frequencia_palavras import frequencia_palavras
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('',), {}),
    (('ola ola',), {'ola': 2}),
    (('Ola OLA ola',), {'ola': 3}),
    (('casa, jardim! casa.',), {'casa': 2, 'jardim': 1}),
    (('a b c',), {'a': 1, 'b': 1, 'c': 1}),
    (('olá mundo, olá',), {'olá': 2, 'mundo': 1}),
])
def test_caso(args, esperado):
    assert frequencia_palavras(*args) == esperado
