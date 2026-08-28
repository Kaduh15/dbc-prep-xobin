import pytest
from solution_ex054_maioridade import contagem_maioridade


@pytest.mark.parametrize(
    "anos, ano_atual, esperado",
    [
        ([2000, 2005, 2015, 1990, 2012, 2008, 2010], 2023, (3, 4)),
        ([1990, 1991], 2023, (2, 0)),
        ([2015, 2016], 2023, (0, 2)),
        ([2005], 2023, (1, 0)),
        ([2004, 2023], 2023, (1, 1)),
        ([], 2023, (0, 0)),
        ([2005, 2006], 2023, (1, 1)),
        ([1995], 2023, (1, 0)),
    ],
)
def test_contagem_maioridade(anos, ano_atual, esperado):
    assert contagem_maioridade(anos, ano_atual) == esperado
