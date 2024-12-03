# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
from typing import List, Union


def find_uniq_1(arr: List) -> Union[int, float]:
    return [el for el in set(arr) if arr.count(el) == 1][0]


def find_uniq_2(arr: List) -> Union[int, float]:
    return min(set(arr), key=arr.count)


if __name__ == "__main__":
    tests = {
        1: ([1, 1, 1, 2, 1, 1], 2),
        2: ([0, 0, 0.55, 0, 0], 0.55),
        3: ([3, 10, 3, 3, 3], 10),
    }
    for t in tests.keys():
        assert find_uniq_1(tests[t][0]) == tests[t][1]
        assert find_uniq_2(tests[t][0]) == tests[t][1]
