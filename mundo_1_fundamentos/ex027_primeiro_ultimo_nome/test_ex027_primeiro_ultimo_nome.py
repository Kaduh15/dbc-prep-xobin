from solution_ex027_primeiro_ultimo_nome import primeiro_ultimo_nome
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('João Silva',), ('João', 'Silva')),
    (('Maria Clara Souza',), ('Maria', 'Souza')),
    (('Ana',), ('Ana', 'Ana')),
    (('  Pedro  Henrique  ',), ('Pedro', 'Henrique')),
    (('',), ('', '')),
    (('   ',), ('', '')),
    (('A B C D',), ('A', 'D')),
    (('   Ana   ',), ('Ana', 'Ana')),
])
def test_caso(args, esperado):
    assert primeiro_ultimo_nome(*args) == esperado
