# Practice (8 points for each):
#
# Given a list of numbers, write a list comprehension that produces a copy of the list.
# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
# Solve the task above using filter() with a lambda function.
# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
# Bonus practice (15 points for each):
# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
# Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.

from functools import reduce

num_1 = [1,2,3,4,5]
num_2 = [n for n in num_1]
num_3 = list(range(1,11))
num_4 = [num for num in num_3 if num %2==0]
num_lam = list(filter(lambda x: (x%2 == 0), num_3))
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruits = sorted(fruits, key=lambda index : index[1])
digits = [1,2,3,4,5]
sum_1 = reduce((lambda x,y: x*y), digits)
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [n for n in list_of_lists for n in n]
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {value:key for key,value in dict_1.items()}



