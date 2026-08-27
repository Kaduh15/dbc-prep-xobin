import pytest

from solution import ordem_apresentacao


@pytest.mark.parametrize(
    "alunos,indices,esperado",
    [
        (
            ["Ana", "Bia", "Caio", "Duda"],
            [1, 3, 0, 2],
            ["Bia", "Duda", "Ana", "Caio"],
        ),
        (["Ana", "Bia", "Caio", "Duda"], [0, 1, 2, 3], ["Ana", "Bia", "Caio", "Duda"]),
        (["Ana", "Bia", "Caio", "Duda"], [3, 2, 1, 0], ["Duda", "Caio", "Bia", "Ana"]),
        (["Ana"], [0], ["Ana"]),
    ],
)
def test_ordem_apresentacao(alunos, indices, esperado):
    assert ordem_apresentacao(alunos, indices) == esperado