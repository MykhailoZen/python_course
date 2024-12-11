# Set up a virtual environment for your project.
# Install the pytest library using pip.
# Create a new test file named test_math.py.
# Write a test function that adds two numbers and returns the value. Create a test  to verify that the function behaves
# correctly for different input values using assert statement.
# Create a class that represents a basic calculator with methods for addition, subtraction, multiplication, and division.
# Write tests to verify each method('s correctness, considering edge cases like division by zero. Use Pytest assertions to'
#                                   ' validate the expected behavior.)
# Advanced task (optional): Test that division method of the Calculator class raises ZeroDivisionError when zero is
# passed as the second argument. The test should PASS.
from typing import Union

import pytest


def add_numbers(a: int, b: int) -> int:
    return a + b


@pytest.mark.parametrize("a, b, ex", [(1, 2, 3), (3, 4, 7), (-5, 6, 1), (7, 0, 7)])
def test_add_numbers(a: int, b: int, ex: int):
    assert add_numbers(a, b) == ex, f"The summ is not equal to {ex}"


class Calculator:
    @classmethod
    def addition(cls, a: Union[int, float], b: Union[int, float]):
        return a + b

    @classmethod
    def subtraction(cls, a: Union[int, float], b: Union[int, float]):
        return a - b

    @classmethod
    def multiplication(cls, a: Union[int, float], b: Union[int, float]):
        return a * b

    @classmethod
    def division(cls, a: Union[int, float], b: Union[int, float]):
        return a / b


@pytest.mark.parametrize("a, b, ex", [(1, 2, 3), (3, 4, 7), (-5, 6, 1), (7, 0, 7)])
def test_addition(a: int, b: int, ex: int):
    assert Calculator.addition(a, b) == ex, f"The summ is not equal to {ex}"

@pytest.mark.P0
@pytest.mark.parametrize("a, b, ex", [(2, 1, 1), (100, 50, 50), (-5, -1, -4), (7, 0, 7)])
def test_subtraction(a: int, b: int, ex: int):
    assert Calculator.subtraction(a, b) == ex, f"The result is not equal to {ex}"


@pytest.mark.P2
@pytest.mark.parametrize("a, b, ex", [(2, 2, 4), (5, 5, 25), (-5, -1, 5), (7, 0, 0)])
def test_multiplication(a: int, b: int, ex: int):
    assert Calculator.multiplication(a, b) == ex, f"The result is not equal to {ex}"


@pytest.mark.parametrize("a, b, ex", [(7, 2, 3.5), (5, 5, 1), (-50, 2, -25)])
def test_division(a: int, b: int, ex: int):
    assert Calculator.division(a, b) == ex, f"The result is not equal to {ex}"


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as context:
        Calculator.division(7, 0)
    assert str(context.value) == 'division by zero', 'Something went wrong'
