# Bonus practice (15 points for each):
# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces
# a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
# Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example:
# {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
from typing import List, Union


def flatten_extend(matrix: List[List[int]]) -> List[int]:
    """
    List of lists will be transferred to single list of all items
    @param matrix: list of list containing digits
    @return: single list of all items
    """
    flat_list = []
    for x in matrix:
        flat_list.extend(x)
    return flat_list


def flip_my_dict(f_dict: Union[dict[str, int], dict[int, str]]) -> Union[dict[str, int], dict[int, str]]:
    """
    Return flipped dict v, k -> k, v"
    @param f_dict: dictionary containing pairs: sting, digit
    @return: flipped dictionary where values and keys changed their places
    """
    return dict((v, k) for k, v in f_dict.items())


if __name__ == "__main__":
    my_list = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
    print(flatten_extend(my_list))

    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(flip_my_dict(my_dict))
    print(flip_my_dict(flip_my_dict(my_dict)))
