from solution_ex08_soma_digitos import soma_digitos
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((123,), 6),
    ((0,), 0),
    ((-45,), 9),
    ((9,), 9),
    ((1000,), 1),
    ((7,), 7),
])
def test_caso(args, esperado):
    assert soma_digitos(*args) == esperado
