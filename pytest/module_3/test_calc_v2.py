import time
import pytest
from . import calc_v2 as c


def test_add():
    assert c.add(3, 2) == 5


@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    (
            (31, 21, 52),
            (0.6, 4.8, 5.4)
    )
)
def test_add_parametrized(a, b, expected):
    assert c.add(a, b) == pytest.approx(expected)


def test_calc_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        c.divide(8, 0)

def test_calc_divide():
    time.sleep(10)
    assert c.divide(10, 2) == 5
