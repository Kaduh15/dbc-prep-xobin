from solution_ex025_tem_silva import tem_silva
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('João Silva Pereira',), True),
    (('MARIA DA SILVA',), True),
    (('Ana Souza',), False),
    (('Silvania',), True),
    (('',), False),
    (('sILvA',), True),
    (('João sILVANIA',), True),
    (('Santo',), False),
    (('Silva Santos',), True),
    (('   da silva   ',), True),
    (('José',), False),
])
def test_caso(args, esperado):
    assert tem_silva(*args) == esperado
