from solution_ex02_prazo_projeto import prazo_projeto
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((['junior'], 10), 1.0),
    ((['junior', 'pleno'], 30), 1.0),
    (([], 100), None),
    ((['senior'], 15), 0.5),
    ((['lider'], 80), 2.0),
    ((['junior', 'junior'], 20), 1.0),
    ((['pleno', 'senior'], 25), 0.5),
    ((['junior'], 0), 0.0),
])
def test_caso(args, esperado):
    assert prazo_projeto(*args) == esperado
