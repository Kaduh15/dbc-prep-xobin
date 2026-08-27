from solution import inverter_string
import pytest


@pytest.mark.parametrize("args,esperado", [
    (['abc'], 'cba'),
    (['a'], 'a'),
    ([''], ''),
    (['javascript'], 'tpircsavaj'),
    (['Olá'], 'álO')
])
def test_caso(args, esperado):
    assert inverter_string(*args) == esperado
