import pytest

from solution import analisar_valor


@pytest.mark.parametrize(
    "valor,esperado",
    [
        (
            "Python",
            {
                "tipo": "str",
                "so_espacos": False,
                "e_numero": False,
                "e_alfabetico": True,
                "e_alfanumerico": True,
                "em_maiusculas": False,
                "em_minusculas": True,
                "capitalizada": True,
            },
        ),
        (
            "1234",
            {
                "tipo": "str",
                "so_espacos": False,
                "e_numero": True,
                "e_alfabetico": False,
                "e_alfanumerico": True,
                "em_maiusculas": False,
                "em_minusculas": False,
                "capitalizada": False,
            },
        ),
        (
            "   ",
            {
                "tipo": "str",
                "so_espacos": True,
                "e_numero": False,
                "e_alfabetico": False,
                "e_alfanumerico": False,
                "em_maiusculas": False,
                "em_minusculas": False,
                "capitalizada": False,
            },
        ),
        (
            "",
            {
                "tipo": "str",
                "so_espacos": False,
                "e_numero": False,
                "e_alfabetico": False,
                "e_alfanumerico": False,
                "em_maiusculas": False,
                "em_minusculas": False,
                "capitalizada": False,
            },
        ),
    ],
)
def test_analisar_valor(valor, esperado):
    assert analisar_valor(valor) == esperado