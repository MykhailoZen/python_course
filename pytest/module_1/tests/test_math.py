import pytest


# Write a test function that adds two numbers
def adder(a, b):
    return a + b


@pytest.mark.parametrize('a, b, expected', [
    (1, 6, 7),
    (0, 55, 55),
    (-4, 2, -2),
    (-7.5, -3.67, -11.17)
])
def test_sum_correct(a, b, expected):
    assert adder(a, b) == expected


def test_sum_incorrect():
    assert not adder(5, 7) == 2


def test_sum_unsupported_types():
    with pytest.raises(TypeError):
        adder(3, '3')


# Create a class that represents a basic calculator
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


class TestCalculator:
    @pytest.mark.P0
    @pytest.mark.parametrize('a, b, expected', [
        (1, 6, 7),
        (-7.5, -3.67, -11.17)
    ])
    def test_addition_correct(self, a, b, expected):
        assert Calculator.addition(a, b) == expected

    @pytest.mark.parametrize('a, b, expected', [
        (1, 6, -5),
        (7.5, -3.67, 11.17)
    ])
    def test_subtraction_correct(self, a, b, expected):
        assert Calculator.subtraction(a, b) == expected

    @pytest.mark.P0
    @pytest.mark.parametrize('a, b, expected', [
        (1, 6, 6),
        (7.2, -1.5, -10.8),
        (0, 3.5, 0.0)
    ])
    def test_multiplication_correct(self, a, b, expected):
        assert Calculator.multiplication(a, b) == expected

    @pytest.mark.parametrize('a, b, expected', [
        (1, 4, 0.25),
        (7.5, -1.25, -6.0)
    ])
    def test_division_correct(self, a, b, expected):
        assert Calculator.division(a, b) == expected

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            Calculator.division(9, 0)

# run only the multiplication test -> pytest <path_to_file>/test_math.py::TestCalculator::test_multiplication_correct
# run only tests, that are not marked as "P0" -> pytest -m 'not P0'
