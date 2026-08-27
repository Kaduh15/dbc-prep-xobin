from solution import contar_caracteres
import pytest


@pytest.mark.parametrize("args,esperado", [
    (['banana'], {'b': 1, 'a': 3, 'n': 2}),
    ([''], {}),
    (['aA'], {'a': 1, 'A': 1}),
    (['aba'], {'a': 2, 'b': 1})
])
def test_caso(args, esperado):
    assert contar_caracteres(*args) == esperado
