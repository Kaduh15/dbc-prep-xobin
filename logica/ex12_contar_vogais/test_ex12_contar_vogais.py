from solution_ex12_contar_vogais import contar_vogais
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('hello',), 2),
    (('',), 0),
    (('AEIOU',), 5),
    (('try',), 0),
    (('banana',), 3),
    (('Olá',), 1),
])
def test_caso(args, esperado):
    assert contar_vogais(*args) == esperado
