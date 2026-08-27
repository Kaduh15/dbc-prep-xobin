import pytest

from solution import sorteia_aluno


@pytest.mark.parametrize(
    "alunos,indice,esperado",
    [
        (["Ana", "Bia", "Caio", "Duda"], 2, "Caio"),
        (["Ana", "Bia", "Caio", "Duda"], 0, "Ana"),
        (["Ana", "Bia", "Caio", "Duda"], 1, "Bia"),
        (["Ana", "Bia", "Caio", "Duda"], 3, "Duda"),
        (["Solo"], 0, "Solo"),
    ],
)
def test_sorteia_aluno(alunos, indice, esperado):
    assert sorteia_aluno(alunos, indice) == esperado