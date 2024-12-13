# Set up a virtual environment for your project.
# Install the pytest library using pip.
# Create a new test file named test_math.py.
# Write a test function that adds two numbers and returns the value.
# Create a test  to verify that the function behaves correctly for different input values using assert statement.
# Create a class that represents a basic calculator with methods for addition, subtraction, multiplication, and division.
# Write tests to verify each method('s correctness, considering edge cases like division by zero.
# 'Use Pytest assertions to validate the expected behavior.)
# Advanced task (optional): Test that division method of the Calculator class raises ZeroDivisionError
# when zero is passed as the second argument. The test should PASS.

import pytest


def func_add(x, y):
    return x + y


@pytest.mark.parametrize("x, y, adding", [
    (2, 2, 4),
    (0, 88, 88),
    (-21.5, 5, -16.5)
])
def test_func_add(x: int, y: int | float, adding: int | float):
    assert func_add(x, y) == adding, "Hmm... Something went wrong!"


class Calculator:
    @classmethod
    def addition(cls, a: int | float, b: int | float):
        return a + b

    @classmethod
    def subtraction(cls, a: int | float, b: int | float):
        return a - b

    @classmethod
    def multiplication(cls, a: int | float, b: int | float):
        return a * b

    @classmethod
    def division(cls, a: int | float, b: int | float):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

@pytest.mark.P0
@pytest.mark.parametrize('x, y, expected',
                         [(2, 2, 4),
                          (0, 88, 88),
                          (-21.5, 5, -16.5)])
def test_addition(x: int | float, y: int | float, expected: int | float):
    assert Calculator.addition(x, y) == expected, "Hmm... Something went wrong!"


@pytest.mark.parametrize('x, y, expected',
                         [(31, 10, 21),
                          (56, 0, 56),
                          (1.8, 9, -7.2)])
def test_subtraction(x: int | float, y: int | float, expected: int | float):
    assert Calculator.subtraction(x, y) == expected, "Hmm... Something went wrong!"


@pytest.mark.P1
@pytest.mark.parametrize('x, y, expected',
                         [(1, 28, 28),
                          (19, 3,57),
                          (4.6, 30, 138)])
def test_multiplication(x: int | float, y: int | float, expected: int | float):
    assert Calculator.multiplication(x, y) == expected, "Hmm... Something went wrong!"


@pytest.mark.parametrize('x, y, expected',
                         [(68, 4, 17),
                          (27, 3, 9)])
def test_division(x: int | float, y: int | float, expected: int | float):
    assert Calculator.division(x, y) == expected, "Hmm... Something went wrong!"