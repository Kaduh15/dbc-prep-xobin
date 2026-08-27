from solution import contar_vogais
import pytest


@pytest.mark.parametrize("args,esperado", [
    (['hello'], 2),
    (['Banana'], 3),
    (['xyz'], 0),
    (['AEIOU'], 5),
    ([''], 0),
    (['ritmo'], 2)
])
def test_caso(args, esperado):
    assert contar_vogais(*args) == esperado
