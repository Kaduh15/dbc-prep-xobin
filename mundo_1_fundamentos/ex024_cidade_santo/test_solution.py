import pytest

from solution import comeca_com_santo


@pytest.mark.parametrize(
    "cidade,esperado",
    [
        ("Santo Amaro", True),
        ("santos", True),
        ("SANTO ANDRÉ", True),
        ("  Santo Antonio  ", True),
        ("Porto Alegre", False),
        ("Rio de Janeiro", False),
    ],
)
def test_comeca_com_santo(cidade, esperado):
    assert comeca_com_santo(cidade) is esperado