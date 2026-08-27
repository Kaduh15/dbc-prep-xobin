import pytest
from solution import validar_sexo


@pytest.mark.parametrize(
    "sexo, esperado",
    [
        ("M", True),
        ("F", True),
        ("m", False),
        ("f", False),
        ("X", False),
        ("", False),
        ("MF", False),
    ],
)
def test_validar_sexo(sexo, esperado):
    assert validar_sexo(sexo) == esperado
