import pytest
from solution import analisar_pessoas


@pytest.mark.parametrize(
    "pessoas, esperado",
    [
        (
            [("Ana", 30, "F"), ("Bruno", 35, "M"), ("Carla", 19, "F"), ("Diego", 40, "M")],
            (31.0, "Diego", 1),
        ),
        (
            [("Alice", 25, "F"), ("Bob", 20, "M")],
            (22.5, "Bob", 0),
        ),
        (
            [("Ana", 30, "F"), ("Bia", 22, "F")],
            (26.0, "", 0),
        ),
        (
            [("Marina", 18, "F"), ("Lucas", 19, "M"), ("Pedro", 50, "M")],
            (29.0, "Pedro", 1),
        ),
    ],
)
def test_analisar_pessoas(pessoas, esperado):
    assert analisar_pessoas(pessoas) == esperado
