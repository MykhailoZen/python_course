import pytest

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Tests for add_numbers function
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, -5) == -10

# Calculator class with basic methods
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

# Tests for Calculator class
def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-2, -3) == -5
    assert calc.add(0, 5) == 5

def test_calculator_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-2, -3) == 1
    assert calc.subtract(0, 5) == -5

def test_calculator_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0

def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2
    assert calc.divide(-6, 3) == -2
    assert calc.divide(0, 5) == 0

# Advanced test: Check division by zero
def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
