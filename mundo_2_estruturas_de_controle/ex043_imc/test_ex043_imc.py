import pytest

from solution_ex043_imc import imc


@pytest.mark.parametrize(
    "args, esperado",
    [
        # casos de exemplo (altura 1.75)
        pytest.param((50, 1.75), 'Abaixo do Peso'),
        pytest.param((70, 1.75), 'Peso Ideal'),
        pytest.param((90, 1.75), 'Sobrepeso'),
        pytest.param((110, 1.75), 'Obesidade'),
        pytest.param((130, 1.75), 'Obesidade Morbida'),
        pytest.param((60, 1.75), 'Peso Ideal'),
        # extremos: limites exatos 18.5 / 25 / 30 / 40 (altura = 2 => imc = peso / 4)
        pytest.param((73, 2), 'Abaixo do Peso'),   # 18.25 abaixo de 18.5
        pytest.param((74, 2), 'Peso Ideal'),       # 18.5 exato (limite inclusivo)
        pytest.param((90, 2), 'Peso Ideal'),       # 22.5
        pytest.param((99, 2), 'Peso Ideal'),       # 24.75
        pytest.param((100, 2), 'Sobrepeso'),       # 25 exato (limite inclusivo)
        pytest.param((101, 2), 'Sobrepeso'),       # 25.25 acima de 25
        pytest.param((110, 2), 'Sobrepeso'),       # 27.5
        pytest.param((119, 2), 'Sobrepeso'),       # 29.75
        pytest.param((120, 2), 'Obesidade'),       # 30 exato (limite inclusivo)
        pytest.param((130, 2), 'Obesidade'),       # 32.5
        pytest.param((159, 2), 'Obesidade'),       # 39.75 abaixo de 40
        pytest.param((160, 2), 'Obesidade Morbida'),  # 40 exato (limite inclusivo)
        pytest.param((200, 2), 'Obesidade Morbida'),  # 50 acima de 40
    ],
)
def test_imc(args, esperado):
    assert imc(*args) == esperado
