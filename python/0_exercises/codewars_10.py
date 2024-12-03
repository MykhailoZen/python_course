# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become
# positives.
#
# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# You can assume that all values are integers. Do not mutate the input array.
from typing import List


def invert(lst: List) -> List:
    return [-x for x in lst]


if __name__ == "__main__":
    tests = {
        1: ([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]),
        2: ([1, -2, 3, -4, 5], [-1, 2, -3, 4, -5]),
        3: ([], []),
    }
    for t in tests.keys():
        assert invert(tests[t][0]) == tests[t][1]
