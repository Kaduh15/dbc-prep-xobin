from solution_ex026_letra_a import analisar_letra_a
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('Arara Azul',), (4, 0, 6)),
    (('Mariana',), (3, 1, 6)),
    (('xyz',), (0, -1, -1)),
    (('',), (0, -1, -1)),
    (('AaA',), (3, 0, 2)),
    (('aaaa',), (4, 0, 3)),
    (('A',), (1, 0, 0)),
    (('a',), (1, 0, 0)),
    (('banana',), (3, 1, 5)),
    (('XYZYX',), (0, -1, -1)),
    (('casa amarela',), (5, 1, 11)),
])
def test_caso(args, esperado):
    assert analisar_letra_a(*args) == esperado
