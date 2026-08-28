import pytest
from solution_ex056_analise_pessoas import analisar_pessoas


@pytest.mark.parametrize(
    "pessoas, esperado",
    [
        ([('Ana', 30, 'F'), ('Bruno', 35, 'M'), ('Carla', 19, 'F'), ('Diego', 40, 'M')], (31.0, 'Diego', 1)),
        ([('Alice', 25, 'F'), ('Bob', 20, 'M')], (22.5, 'Bob', 0)),
        ([('Ana', 30, 'F'), ('Bia', 22, 'F')], (26.0, '', 0)),
        ([('Marina', 18, 'F'), ('Lucas', 19, 'M'), ('Pedro', 50, 'M')], (29.0, 'Pedro', 1)),
        ([('Ana', 20, 'F'), ('Bia', 19, 'F')], (19.5, '', 1)),
        ([('Eva', 30, 'F'), ('Eva2', 30, 'F')], (30.0, '', 0)),
        ([('Rui', 22, 'M')], (22.0, 'Rui', 0)),
        ([('Lu', 15, 'F'), ('Lia', 16, 'F')], (15.5, '', 2)),
    ],
)
def test_analisar_pessoas(pessoas, esperado):
    assert analisar_pessoas(pessoas) == esperado
