# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
# First argument is an array of numbers and the second is the divisor.
#
# Example(Input1, Input2 --> Output)
# [1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]
from typing import List


def divisible_by(numbers: List[int], divisor: int) -> List[int]:
    return [x for x in numbers if x % divisor == 0]


if __name__ == "__main__":
    tests = {
        1: ([1, 2, 3, 4, 5, 6], 2, [2, 4, 6]),
        2: ([1, 2, 3, 4, 5, 6], 3, [3, 6]),
        3: ([0, 1, 2, 3, 4, 5, 6], 4, [0, 4]),
        4: ([0], 4, [0]),
        5: ([1, 3, 5], 2, []),
        6: ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    }
    for t in tests.keys():
        assert divisible_by(tests[t][0], tests[t][1]) == tests[t][2]
