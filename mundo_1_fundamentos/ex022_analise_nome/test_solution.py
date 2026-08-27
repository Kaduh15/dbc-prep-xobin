import pytest

from solution import analisar_nome


@pytest.mark.parametrize(
    "nome,maiusculas,minusculas,total_letras,primeiro_nome",
    [
        ("Maria Silva", "MARIA SILVA", "maria silva", 10, 5),
        ("JOAO PEREIRA", "JOAO PEREIRA", "joao pereira", 11, 4),
        ("A", "A", "a", 1, 1),
        ("Ana Clara de Souza", "ANA CLARA DE SOUZA", "ana clara de souza", 15, 3),
    ],
)
def test_analisar_nome(nome, maiusculas, minusculas, total_letras, primeiro_nome):
    assert analisar_nome(nome) == (maiusculas, minusculas, total_letras, primeiro_nome)