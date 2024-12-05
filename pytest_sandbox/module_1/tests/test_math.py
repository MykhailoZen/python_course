import pytest
from pytest_sandbox.module_1.test_calculator import Calculator


def add_two_numbers(x, y):
    return x + y


@pytest.mark.parametrize(
    ('input1','input2','expected'),
    (
            pytest.param(1,1,2, marks=pytest.mark.p0),
            (2,2,4),
            (3,3,6),
            (4,2,6),
            (1,9,10),
    )
                         )
def test_add_two_numbers(input1, input2, expected):
    assert add_two_numbers(input1, input2) == expected


@pytest.mark.parametrize(
        ('input1', 'input2', 'expected'),
        (
                pytest.param(2, 2, 4, marks=pytest.mark.p0),
                (5, 5, 25),
                (10, 10, 100),
                (25, 5, 125),
        )
    )
def test_multiplication_two_numbers(input1, input2, expected):
        assert Calculator.multiplication(input1, input2) == expected

'''
Task: Run all tests from the tests folder.
pytest pytest_sandbox/module_1/tests

Task: Run only the multiplication test from the test_math.py file using the test name filtering option.
pytest pytest_sandbox/module_1/tests/test_math.py::test_multiplication_two_numbers

Run only P0 cases: 
pytest -m p0 pytest_sandbox/module_1/tests

Use marker filtering to run only tests, that are not marked as "P0".
pytest -m "not p0" pytest_sandbox/module_1/tests

'''