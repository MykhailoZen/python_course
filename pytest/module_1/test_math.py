##### Console Commands: #####
# Run specific file verbose:                pytest test_math.py -v
# Run specific test function in the file:   pytest test_math.py::test_add_parametrized

import pytest


def add(a, b):
    return a + b

#Simple test
def test_add():
    assert add(3, 2) == 5


# Parametrized test
@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    (
            (31, 21, 52),
            (0.6, 4.8, 5.4)
    )
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == pytest.approx(expected)
