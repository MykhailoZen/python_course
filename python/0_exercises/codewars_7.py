# Complete the square sum function so that it squares each number passed into it and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because
# 1^2 + 2^2 + 2^2 =9
from typing import List


def square_sum(numbers: List[int]) -> int:
    return sum(x**2 for x in numbers)


if __name__ == "__main__":
    tests = {
        1: ([0, 3, 4, 5], 50),
        2: ([], 0),
        3: ([-1, -2], 5),
        4: ([-1, 0, 1], 2),
        5: ([1, 2], 5),
    }
    for t in tests.keys():
        assert square_sum(tests[t][0]) == tests[t][1]
