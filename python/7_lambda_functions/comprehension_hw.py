from functools import reduce

# Given a list of numbers, write a list comprehension that produces a copy of the list.
list_hanna = ['Alex', 'Hanna', 'Ksu', 'Olha', 'Inna', 'Helen']
list_anna = [vl for vl in list_hanna]

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
print([even for even in range(1, 12) if even % 2 == 0])

# Solve the task above using filter() with a lambda function.
print(list(filter(lambda x: x % 2 == 0, range(1, 12))))

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
dict1 = [("apple", 50), ("banana", 10), ("cherry", 30)]
print(sorted(dict1, key=lambda x: x[1]))

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the
# standard library and a lambda function.
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single
# list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list2 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
list_new = [x for internal_list in list2 for x in internal_list]
print(list_new)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.

dict2 = {'a': 1, 'b': 2, 'c': 3}
dict_new = {y: x for x, y in dict2.items()}
print(dict_new)
