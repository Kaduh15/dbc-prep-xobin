import pytest

from solution import ola_mundo


@pytest.mark.parametrize("esperado", ["Olá, mundo!"])
def test_ola_mundo(esperado):
    assert ola_mundo() == esperado