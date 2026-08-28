import pytest

from solution_ex019_sorteio_aluno import sorteia_aluno


@pytest.mark.parametrize(
    "alunos,indice,esperado",
    [
        (['Ana', 'Bia', 'Caio', 'Duda'], 2, 'Caio'),
        (['Ana', 'Bia', 'Caio', 'Duda'], 0, 'Ana'),
        (['Ana', 'Bia', 'Caio', 'Duda'], 1, 'Bia'),
        (['Ana', 'Bia', 'Caio', 'Duda'], 3, 'Duda'),
        (['Solo'], 0, 'Solo'),
        (['a', 'b', 'c', 'd', 'e', 'f'], 5, 'f'),
        (['a', 'b', 'c'], 2, 'c'),
    ],
)
def test_sorteia_aluno(alunos, indice, esperado):
    assert sorteia_aluno(alunos, indice) == esperado
