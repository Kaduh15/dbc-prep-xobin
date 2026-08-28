from solution_ex01_fizzbuzz import fizzbuzz
import pytest


@pytest.mark.parametrize("args,esperado", [
    ((15,), 'FizzBuzz'),
    ((3,), 'Fizz'),
    ((5,), 'Buzz'),
    ((1,), '1'),
    ((30,), 'FizzBuzz'),
    ((0,), 'FizzBuzz'),
    ((-3,), 'Fizz'),
    ((45,), 'FizzBuzz'),
    ((7,), '7'),
])
def test_caso(args, esperado):
    assert fizzbuzz(*args) == esperado
