# Given a list of numbers, write a list comprehension that produces a copy of the list.
# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
# Solve the task above using filter() with a lambda function.
# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.

from functools import reduce

nums = [1, 2, 3, 4, 5]
nums_new = [x for x in nums]
print(nums_new, '\n--------------------------')

nums = list(range(1, 11))
print(nums)
nums_new = [x for x in nums if x % 2 == 0]
print(nums_new, '\n--------------------------')

nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x, nums)), '\n--------------------------')

nums = list(range(1, 11))
print(list(filter(lambda x: x % 2 == 0 ,nums)), '\n--------------------------')

mylist = [("apple", 50), ("banana", 10), ("cherry", 30)]
print(sorted(mylist, key=lambda x: x[1]), '\n--------------------------')

nums = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, nums), '\n--------------------------')
