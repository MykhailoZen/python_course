import pytest


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