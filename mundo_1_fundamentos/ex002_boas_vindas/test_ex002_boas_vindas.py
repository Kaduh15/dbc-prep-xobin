from solution_ex002_boas_vindas import boas_vindas
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    (("João",), "Olá, João! Seja muito bem-vindo(a)!"),
    (("Maria",), "Olá, Maria! Seja muito bem-vindo(a)!"),
    (("",), "Olá, ! Seja muito bem-vindo(a)!"),
    (("Ana Clara",), "Olá, Ana Clara! Seja muito bem-vindo(a)!"),
    ((" ",), "Olá,  ! Seja muito bem-vindo(a)!"),
    (("Zé",), "Olá, Zé! Seja muito bem-vindo(a)!"),
    ],
)
def test_boas_vindas(args, esperado):
    assert boas_vindas(*args) == esperado
