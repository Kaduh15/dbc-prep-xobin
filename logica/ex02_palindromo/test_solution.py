from solution import palindromo
import pytest


@pytest.mark.parametrize("args,esperado", [
    (['ana'], True),
    (['hello'], False),
    (['A man a plan a canal Panama'], True),
    ([''], True),
    (['anA'], True),
    (['never odd or even'], True),
    (['java'], False)
])
def test_caso(args, esperado):
    assert palindromo(*args) == esperado
