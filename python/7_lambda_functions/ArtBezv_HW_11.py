import functools

#Task 1
#Given a list of numbers, write a list comprehension that produces a copy of the list.
nums = [3, 5, 7, 9, 11, 13]
result_nums = [x for x in nums]
print(result_nums)


#Task 2
#Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
#numbers = range(1,11)
numbers_list = [x for x in range(1, 11) if x % 2 == 0]
print(numbers_list)


#Task 3
#Solve the task above using filter() with a lambda function.
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(even_numbers)


# Task4
# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
result_list = list(sorted(fruits_list, key=lambda x: x[1]))
print(result_list)


#Task 5
#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function
nums_list = [1, 2, 3, 4, 5]
result_nums_list = functools.reduce(lambda x, y: x * y, nums_list)
print(result_nums_list)

#Bonus practice
#Task 1
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
overall_list = [item for innerlist in list_of_lists for item in innerlist]
print(overall_list)



