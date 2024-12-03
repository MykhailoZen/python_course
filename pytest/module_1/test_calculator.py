import pytest


class Calculator:
    @staticmethod
    def addition(x,y):
        return x+y

    @staticmethod
    def subtraction(x,y):
        return x-y

    @staticmethod
    def multiplication(x,y):
        return x*y

    @staticmethod
    def division(x,y):
        return x/y

@pytest.mark.parametrize(
        ('input1', 'input2', 'expected'),
        (
                (1, 1, 2),
                (2, 2, 4),
                (3, 3, 6),
                (4, 2, 6),
                (1, 9, 10),
                (10, 0, 10),
        )
    )
def test_addition(input1, input2, expected):
        assert Calculator.addition(input1, input2) == expected

@pytest.mark.parametrize(
        ('input1', 'input2', 'expected'),
        (
                (2, 1, 1),
                (100, 50, 50),
                (50, 4, 46),
                (1, 0, 1),
        )
    )
def test_subtraction(input1, input2, expected):
        assert Calculator.subtraction(input1, input2) == expected


@pytest.mark.parametrize(
        ('input1', 'input2', 'expected'),
        (
                (2, 2, 4),
                (5, 5, 25),
                (10, 10, 100),
                (25, 5, 125),
        )
    )
def test_multiplication(input1, input2, expected):
        assert Calculator.multiplication(input1, input2) == expected


@pytest.mark.parametrize(
        ('input1', 'input2', 'expected'),
        (
                (4, 2, 2),
                (25, 5, 5),
                (100, 10, 10),
                (100, 3, 33.333333333333336),
                pytest.param(25, 0, 0, marks=pytest.mark.xfail(reason="Division by zero")),
        )
    )
def test_division(input1, input2, expected):
        assert Calculator.division(input1, input2) == expected


def test_division_by_zero():
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        Calculator.division(5, 0)
    assert str(excinfo.value) == "division by zero"