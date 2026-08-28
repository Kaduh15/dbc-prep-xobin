import pytest

from solution_ex024_cidade_santo import comeca_com_santo


@pytest.mark.parametrize(
    "cidade,esperado",
    [
        ('Santo Amaro', True),
        ('santos', True),
        ('SANTO ANDRÉ', True),
        ('  Santo Antonio  ', True),
        ('Porto Alegre', False),
        ('Rio de Janeiro', False),
        ('Santo', True),
        ('SANTOS', True),
        ('santorini', True),
        ('', False),
        ('Asantos', False),
    ],
)
def test_comeca_com_santo(cidade, esperado):
    assert comeca_com_santo(cidade) is esperado
