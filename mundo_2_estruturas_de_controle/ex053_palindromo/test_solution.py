import pytest
from solution import eh_palindromo


@pytest.mark.parametrize(
    "frase, esperado",
    [
        ("arara", True),
        ("Ana", True),
        ("a sacada da casa", True),
        ("socorram me subi no onibus em marrocos", True),
        ("Roma me tem amor", True),
        ("banana", False),
        ("palindromo", False),
    ],
)
def test_eh_palindromo(frase, esperado):
    assert eh_palindromo(frase) == esperado
