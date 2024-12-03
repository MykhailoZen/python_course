# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
from typing import List


def count_positives_sum_negatives_1(arr: List) -> List:
    pos_count = 0
    neg_sum = 0
    if len(arr) != 0:
        for x in arr:
            if x > 0:
                pos_count += 1
            else:
                neg_sum += x
        return [pos_count, neg_sum]
    else:
        return []


def count_positives_sum_negatives_2(arr: List) -> List:
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


if __name__ == "__main__":
    tests = {
        1: ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], [10, -65]),
        2: ([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14], [8, -50]),
        3: ([1], [1, 0]),
        4: ([-1], [0, -1]),
        5: ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0]),
        6: ([], []),
    }
    for t in tests.keys():
        assert count_positives_sum_negatives_1(tests[t][0]) == tests[t][1]
        assert count_positives_sum_negatives_2(tests[t][0]) == tests[t][1]
