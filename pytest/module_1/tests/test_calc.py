from .. import calc as c
import pytest


class TestsCalc:
    @pytest.mark.P0
    @pytest.mark.parametrize(
        ('a', 'b', 'expected'),
        (
                (31, 21, 52),
                (0.6, 4.8, 5.4)
        )
    )
    def test_calc_add(self, a, b, expected):
        assert c.add(a, b) == pytest.approx(expected)

    @pytest.mark.P0
    @pytest.mark.parametrize(
        ('a', 'b', 'expected'),
        (
                (751, 1, 750),
                (34, 51, -17)
        )
    )
    def test_calc_subtract(self, a, b, expected):
        assert c.subtract(a, b) == expected

    @pytest.mark.parametrize(
        ('a', 'b', 'expected'),
        (
                (-9, 2, -18),
                (7.8, 1.1, 8.58)
        )
    )
    def test_calc_multiply(self, a, b, expected):
        assert c.multiply(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize(
        ('a', 'b', 'expected'),
        (
                (50, 2, 25),
                (100, 500, 0.2)
        )
    )
    def test_calc_divide(self, a, b, expected):
        assert c.divide(a, b) == expected

    def test_calc_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            c.divide(8, 0)
