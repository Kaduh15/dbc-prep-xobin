from solution_ex004_tipo_primitivo import analisar_valor
import pytest


@pytest.mark.parametrize(
    "args,esperado",
    [
    (('Python',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": True, "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": False, "capitalizada": True}),
    (('1234',), {"tipo": "str", "so_espacos": False, "e_numero": True, "e_alfabetico": False, "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": False, "capitalizada": False}),
    (('   ',), {"tipo": "str", "so_espacos": True, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": False, "em_maiusculas": False, "em_minusculas": False, "capitalizada": False}),
    (('',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": False, "em_maiusculas": False, "em_minusculas": False, "capitalizada": False}),
    (('ABC',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": True, "e_alfanumerico": True, "em_maiusculas": True, "em_minusculas": False, "capitalizada": False}),
    (('abc',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": True, "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": True, "capitalizada": False}),
    (('Hello World',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": False, "em_maiusculas": False, "em_minusculas": False, "capitalizada": True}),
    (('12A',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": True, "em_maiusculas": True, "em_minusculas": False, "capitalizada": True}),
    (('123abc',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": True, "em_maiusculas": False, "em_minusculas": True, "capitalizada": False}),
    (('   X',), {"tipo": "str", "so_espacos": False, "e_numero": False, "e_alfabetico": False, "e_alfanumerico": False, "em_maiusculas": True, "em_minusculas": False, "capitalizada": True}),
    ],
)
def test_analisar_valor(args, esperado):
    assert analisar_valor(*args) == esperado
