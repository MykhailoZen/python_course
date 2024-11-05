# Practice (8 points for each):
# Given a list of numbers, write a list comprehension that produces a copy of the list.
# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
# Solve the task above using filter() with a lambda function.
# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the
# standard library and a lambda function.

# Bonus practice (15 points for each):
# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single
# list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
from functools import reduce
from typing import Union


def flip_the_dictionary(f_dict: Union[dict[str: int], dict[int: str]]) -> Union[dict[str: int], dict[int: str]]:
    """
    Flip the dictionary
    @param f_dict: dictionary which need to flip
    @return: dictionary with val:key couples
    """
    return {f_dict[key]: key for key in f_dict}


if __name__ == '__main__':
    list_1 = [1, 6, 8, 9, 7]
    print([item for item in list_1])
    print(list(map(lambda x: x, list_1)))

    print([x for x in range(1, 11) if x % 2 == 0])
    print(list(filter(lambda x: x % 2 == 0, range(1, 11))))

    print(sorted([("apple", 50), ("banana", 10), ("cherry", 30)], key=lambda x: x[1]))
    print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

    list_2 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
    print([item for x in list_2 for item in x])
    print(reduce(lambda x, y: x + y, list_2))

    dict_1 = {'a': 1, 'b': 2, 'c': 3}
    print(flip_the_dictionary(dict_1))
    print(flip_the_dictionary(flip_the_dictionary(dict_1)))
