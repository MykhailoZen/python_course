# Take an array and remove every second element from the array. Always keep the first element and start removing with
# the next element.
#
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
#
# None of the arrays will be empty, so you don't have to worry about that!
from typing import Any, List


def remove_every_other(my_list: List[Any]) -> List[Any]:
    return my_list[::2]


if __name__ == "__main__":
    tests = {
        1: (["Hello", "Goodbye", "Hello Again"], ["Hello", "Hello Again"]),
        2: ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]),
        3: ([[1, 2]], [[1, 2]]),
        4: ([["Goodbye"], {"Great": "Job"}], [["Goodbye"]]),
    }
    for t in tests.keys():
        assert remove_every_other(tests[t][0]) == tests[t][1]
