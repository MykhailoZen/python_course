# 1 Set up a virtual environment for your project.
# 2 Install the pytest library using pip.
# 3 Create a new test file named test_math.py.
# 4 Write a test function that adds two numbers and returns the value. Create a test to verify that the function
# behaves correctly for different input values using assert statement.
# 5 Create a class that represents a basic calculator with methods for addition, subtraction, multiplication,
# and division. Write tests to verify each method's correctness, considering edge cases like division by zero.
# Use Pytest assertions to validate the expected behavior.
# 6 Advanced task (optional): Test that division method of the Calculator class raises ZeroDivisionError when zero is
# passed as the second argument. The test should PASS.

from typing import Union
import pytest


def sum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


@pytest.mark.parametrize("a, b, result", [(1, 3, 4), (-1, 3, 2), (-1.1, -3.1, -4.2)])
def test_sum(a: Union[int, float], b: Union[int, float], result: Union[int, float]):
    assert sum(a, b) == result, "sum function behaves not correctly for different input values"

class Calculator:

    @classmethod
    def addition(cls, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

    @classmethod
    def subtraction(cls, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

    @classmethod
    def multiplication(cls, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

    @classmethod
    def division(cls, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a / b

@pytest.mark.parametrize("a, b, result", [(1, 3, 4), (-1, 3, 2), (-1.1, -3.1, -4.2)])
def test_addition(a: Union[int, float], b: Union[int, float], result: Union[int, float]):
    assert Calculator.addition(a, b) == result, "---fail addition---"

@pytest.mark.parametrize("a, b, result", [(3, 1, 2), (-1, 3, -4), (-1.1, 3.1, -4.2)])
def test_subtraction(a: Union[int, float], b: Union[int, float], result: Union[int, float]):
    assert Calculator.subtraction(a, b) == result, "---fail subtraction---"

@pytest.mark.parametrize("a, b, result", [(3, 1, 3), (-1, 3, -3), (3, 3, 9)])
def test_multiplication(a: Union[int, float], b: Union[int, float], result: Union[int, float]):
    assert Calculator.multiplication(a, b) == result, "---fail multiplication---"

@pytest.mark.parametrize("a, b, result", [(3, 1, 3), (-3, 3, -1)])
def test_division(a: Union[int, float], b: Union[int, float], result: Union[int, float]):
    assert Calculator.division(a, b) == result, "---fail division---"

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as error:
        Calculator.division(9, 0)
        assert error.value == "division by zero"