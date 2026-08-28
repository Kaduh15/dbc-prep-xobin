import pytest

from solution_ex018_trigonometria import trigonometria


@pytest.mark.parametrize(
    "angulo,seno,cosseno,tangente",
    [
        (0, 0.0, 1.0, 0.0),
        (30, 0.5, 0.8660254037844386, 0.5773502691896257),
        (45, 0.7071067811865475, 0.7071067811865475, 1.0),
        (60, 0.8660254037844386, 0.5, 1.7320508075688767),
        (180, 0.0, -1.0, 0.0),
        (22.5, 0.3826834323650898, 0.9238795325112867, 0.41421356237309503),
    ],
)
def test_trigonometria(angulo, seno, cosseno, tangente):
    resultado = trigonometria(angulo)
    assert len(resultado) == 3
    assert resultado[0] == pytest.approx(seno)
    assert resultado[1] == pytest.approx(cosseno)
    assert resultado[2] == pytest.approx(tangente)
