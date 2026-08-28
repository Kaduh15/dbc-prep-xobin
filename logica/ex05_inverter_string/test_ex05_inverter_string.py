from solution_ex05_inverter_string import inverter_string
import pytest


@pytest.mark.parametrize("args,esperado", [
    (('hello',), 'olleh'),
    (('',), ''),
    (('abc',), 'cba'),
    (('a',), 'a'),
    (('a man',), 'nam a'),
    (('olá mundo',), 'odnum álo'),
])
def test_caso(args, esperado):
    assert inverter_string(*args) == esperado
