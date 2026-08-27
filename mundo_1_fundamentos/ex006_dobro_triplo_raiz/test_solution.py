import pytest

from solution import dobro_triplo_raiz


@pytest.mark.parametrize(
    "n,esperado",
    [
        (9, (18.0, 27.0, 3.0)),
        (4, (8.0, 12.0, 2.0)),
        (0, (0.0, 0.0, 0.0)),
        (2, (4.0, 6.0, pytest.approx(1.4142135623730951))),
    ],
)
def test_dobro_triplo_raiz(n, esperado):
    dobro, triplo, raiz = dobro_triplo_raiz(n)
    assert (dobro, triplo) == (esperado[0], esperado[1])
    assert raiz == esperado[2]