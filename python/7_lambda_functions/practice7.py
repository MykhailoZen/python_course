# Given a list of numbers, write a list comprehension that produces a copy of the list.
# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
# Solve the task above using filter() with a lambda function.
# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from
# the standard library and a lambda function.

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces
# a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
from functools import reduce

if __name__ == "__main__":
    print([x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    print([x for x in range(1, 12) if x % 2 == 0])
    print(list(filter(lambda x: x % 2 == 0, range(1, 12))))
    print(sorted([("apple", 50), ("banana", 10), ("cherry", 30)], key=lambda x: x[1]))
    print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

    first_list = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
    print([element for inside_list in first_list for element in inside_list])
    print(reduce(lambda x, y: x + y, first_list))

    dict_1 = {'a': 1, 'b': 2, 'c': 3}
    print({value: key for key, value in dict_1.items()})
    print({dict_1[key]: key for key in dict_1})
