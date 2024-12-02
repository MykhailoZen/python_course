# Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# Write a function that calculates the factorial of a number using the functional approach.
# Capitalize the first letter of each word in a sentence "hello world, how are you?".
# Given a list of students and their marks as tuples:
#
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.
import functools


def func1 (list1):
    return [x**2 for x in list1]

def func2 (list1):
    return [x for x in list1 if x % 2 == 0]

def func3 (list1):
    return functools.reduce(lambda x, y: x * y, list1)

def func4 (str1):
    return str1.title()

def func5 (list1):
    return sum([item[1] for item in list1])/len(list1)


if __name__ == "__main__":
    print(func1(list(range(10))))
    print(func2(list(range(10))))
    print(func3([1,2,3]))
    print(func4("hello world, how are you?"))
    print(func5([("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]))
