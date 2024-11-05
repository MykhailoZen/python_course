# Practice (8 points for each):
# Given a list of numbers, write a list comprehension that produces a copy of the list.
# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
# Solve the task above using filter() with a lambda function.
# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce()
# from the standard library and a lambda function.
from functools import reduce

cars = [2, 151, 890]
copy_cars = [x for x in cars]
print(copy_cars)

pills = [x for x in range(1, 11) if x % 2 == 0]
print(pills)

pills = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(pills)

fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
print(sorted(fruits, key=lambda x: x[1]))

my_list = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, my_list))
