import calc as c
import pytest

@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    (
            (31, 21, 52),
            (0.6, 4.8, 5.4)
    )
)
def test_calc_add(a, b, expected):
    assert c.add(a, b) == pytest.approx(expected)

@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    (
            (751, 1, 750),
            (34, 51, -17)
    )
)
def test_calc_subtract(a, b, expected):
    assert c.subtract(a, b) == expected

@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    (
            (-9, 2, -18),
            (7.8, 1.1, 8.58)
    )
)
def test_calc_multiply(a, b, expected):
    assert c.multiply(a, b) == pytest.approx(expected)

@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    (
            (50, 2, 25),
            (100, 500, 0.2)
    )
)
def test_calc_divide(a, b, expected):
    assert c.divide(a, b) == expected

def test_calc_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        c.divide(8, 0)
