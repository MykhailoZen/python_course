# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
#
# The order of the sequence has to stay the same.
#
# Examples:
# # Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]
from typing import List


def distinct_1(seq: List) -> List:
    v = []
    for a in seq:
        if a not in v:
            v.append(a)
    return v


def distinct_2(seq):
    return sorted(set(seq), key=seq.index)


if __name__ == "__main__":
    tests = {
        1: ([1], [1]),
        2: ([1, 2], [1, 2]),
        3: ([1, 1, 2], [1, 2]),
        4: ([1, 1, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        5: ([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7], [1, 2, 3, 4, 5, 6, 7]),
    }
    for t in tests.keys():
        assert distinct_1(tests[t][0]) == tests[t][1]
        assert distinct_2(tests[t][0]) == tests[t][1]
