from solution_ex001_ola_mundo import ola_mundo
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    ((), "Olá, mundo!"),
    ],
)
def test_ola_mundo(args, esperado):
    assert ola_mundo(*args) == esperado

def test_ola_mundo_tipo_e_determinismo():
    s = ola_mundo()
    assert isinstance(s, str)
    assert ola_mundo() == ola_mundo()
