from solution import fizzbuzz
import pytest


@pytest.mark.parametrize("args,esperado", [
    ([1], '1'),
    ([3], 'Fizz'),
    ([5], 'Buzz'),
    ([15], 'FizzBuzz'),
    ([9], 'Fizz'),
    ([10], 'Buzz'),
    ([30], 'FizzBuzz'),
    ([7], '7')
])
def test_caso(args, esperado):
    assert fizzbuzz(*args) == esperado
