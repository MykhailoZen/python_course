"""
1. Create a new test file named test_math.py.
2. Write a test function that adds two numbers and returns the value.
Create a test  to verify that the function behaves correctly for different input values using assert statement.
3. Create a class that represents a basic calculator with methods for addition, subtraction, multiplication, and division.
 Write tests to verify each method's correctness, considering edge cases like division by zero.
 Use Pytest assertions to validate the expected behavior.
4. Advanced task (optional): Test that division method of the Calculator class raises ZeroDivisionError
 when zero is passed as the second argument. The test should PASS.

In the test_math.py file, add a marker "P0" to the addition and multiplication tests.
Use marker filtering to run only tests, that are not marked as "P0".
"""

import pytest

def add(x1: float, x2: float):
    return x1 + x2
@pytest.mark.P0
def test_add():
    assert add(1, 2) == 3
    assert add(1.0, 2) == 3.0
    assert add(1, 2.0) == 3.0
    assert add(0.0, 0) == 0.0
    assert add(-1, 2) == 1
    assert add(-10.0, -5) == -15.0


class Calculator:
    def __init__(self):
        pass
    def addition(self, x1: float, x2: float):
        return x1 + x2

    def subtraction(self, x1: float, x2: float):
        return x1 - x2

    def multiplication(self, x1: float, x2: float):
        return x1 * x2

    def division(self, x1: float, x2: float):
        if x2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x1 / x2

def test_calculator():
    calc = Calculator()
    assert calc.addition(1, 2.0) == 3.0
    assert calc.subtraction(5.0, -3) == 8.0
    assert calc.multiplication(2, 3) == 6
    assert calc.division(9, 1.5) == 6.0

    with pytest.raises(ZeroDivisionError):
        calc.division(1, 0)

# Write a test function to test the multiplication of two numbers in the test_math.py file.
# Run only the multiplication test from the test_math.py file using the test name filtering option.
# pytest module_1/tests/test_math.py::test_multiplication; pytest module_1/tests/test_math.py -k "multiplication"
#pytest -m P0
@pytest.mark.P0
def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(2, 3) == 6
    assert calc.multiplication(-1, 5) == -5
    assert calc.multiplication(0, 10) == 0
    assert calc.multiplication(0.5, 4) == 2.0
    assert calc.multiplication(0, 0) == 0