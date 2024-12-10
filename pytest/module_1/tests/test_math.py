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


def function_adds(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


@pytest.mark.parametrize('x, y, adding', [
    (2, 3, 5),
    (0, 45, 45),
    (9, -7, 2),
    (-6.5, 3.8, -2.7)
])
def test_adding(x, y, adding):
    assert function_adds(x, y) == adding, "The function is not behaving correctly."


class Calculator:
    @classmethod
    def addition(cls, a, b):
        return a + b

    @classmethod
    def subtraction(cls, a, b):
        return a - b

    @classmethod
    def multiplication(cls, a, b):
        return a * b

    @classmethod
    def division(cls, a, b):
        return a / b


@pytest.mark.P0
@pytest.mark.parametrize('x, y, expected',
                         [(2, 5, 7),
                          (0, 7, 7),
                          (-7.5, -3.67, -11.17)])
def test_addition(x, y, expected):
    assert Calculator.addition(x, y) == expected, "The function is not behaving correctly."


@pytest.mark.parametrize('x, y, expected',
                         [(1, 6, -5),
                          (0, 7, -7),
                          (7.5, -3.67, 11.17)])
def test_subtraction(x, y, expected):
    assert Calculator.subtraction(x, y) == expected, "The function is not behaving correctly."


@pytest.mark.P0
@pytest.mark.parametrize('x, y, expected',
                         [(1, 6, 6),
                          (0, 7, 0),
                          (8.8, 2, 17.6)])
def test_multiplication(x, y, expected):
    assert Calculator.multiplication(x, y) == expected, "The function is not behaving correctly."


@pytest.mark.parametrize('x, y, expected',
                         [(6, 2, 3),
                          (16, 8, 2)])
def test_division(x, y, expected):
    assert Calculator.division(x, y) == expected, "The function is not behaving correctly."


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.division(9, 0)

# pytest ./pytest/module_1/test_math.py
# 16 passed in 0.02s
