import functools

#Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [1,4,6,61,78,9,0,-5,45]
copy_numbers = [x for x in numbers]
print(copy_numbers)

#Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
even_numbers = [x for x in range(1,11) if x % 2 == 0]
print(even_numbers)

#Solve the task above using filter() with a lambda function.
even_nums = list(filter(lambda x: x % 2 == 0, range(1,11)))
print(even_nums)

#Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
fruits.sort(key = lambda price: price[1])
print(fruits)

#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
nums = [1, 2, 3, 4, 5]
multiply_nums = functools.reduce(lambda x, y: x*y, nums)
print(multiply_nums)

#Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
more_nums = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
merged_nums = [element for row in more_nums for element in row]
print(merged_nums)

#Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dictionary = {'a': 1, 'b': 2, 'c': 3}
flip_dict = {key:value for value, key in dictionary.items()}
print(flip_dict)
