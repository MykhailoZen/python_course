import pytest
from pytest_sandbox.module_1.test_calculator import Calculator


def add_two_numbers(x, y):
    return x + y

@pytest.mark.parametrize(
    ('input1','input2','expected'),
    (
            (1,1,2),
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
                (2, 2, 4),
                (5, 5, 25),
                (10, 10, 100),
                (25, 5, 125),
        )
    )
def test_multiplication_two_numbers(input1, input2, expected):
        assert Calculator.multiplication(input1, input2) == expected

'''
pytest pytest_sandbox/module_1/tests
pytest pytest_sandbox/module_1/tests/test_math.py::test_multiplication_two_numbers

'''