import pytest

from solution import boas_vindas


@pytest.mark.parametrize(
    "nome,esperado",
    [
        ("João", "Olá, João! Seja muito bem-vindo(a)!"),
        ("Maria", "Olá, Maria! Seja muito bem-vindo(a)!"),
        ("", "Olá, ! Seja muito bem-vindo(a)!"),
    ],
)
def test_boas_vindas(nome, esperado):
    assert boas_vindas(nome) == esperado