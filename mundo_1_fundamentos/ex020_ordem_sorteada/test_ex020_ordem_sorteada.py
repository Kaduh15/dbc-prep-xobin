import pytest

from solution_ex020_ordem_sorteada import ordem_apresentacao


@pytest.mark.parametrize(
    "alunos,indices,esperado",
    [
        (['Ana', 'Bia', 'Caio', 'Duda'], [1, 3, 0, 2], ['Bia', 'Duda', 'Ana', 'Caio']),
        (['Ana', 'Bia', 'Caio', 'Duda'], [0, 1, 2, 3], ['Ana', 'Bia', 'Caio', 'Duda']),
        (['Ana', 'Bia', 'Caio', 'Duda'], [3, 2, 1, 0], ['Duda', 'Caio', 'Bia', 'Ana']),
        (['Ana'], [0], ['Ana']),
        ([], [], []),
        (['a', 'b', 'c'], [2, 1, 0], ['c', 'b', 'a']),
        (['x', 'y'], [1, 0], ['y', 'x']),
    ],
)
def test_ordem_apresentacao(alunos, indices, esperado):
    assert ordem_apresentacao(alunos, indices) == esperado
