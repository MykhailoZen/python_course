# Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# Write a function that calculates the factorial of a number using the functional approach.
# Capitalize the first letter of each word in a sentence "hello world, how are you?".
# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.

from functools import reduce

def square(x):
    return x * x

def even(x):
    return x if x % 2 == 0 else None

def factorial(x):
    return reduce(lambda a, b: a * b, range(1, x + 1))

def apply_to_list(func, values):
    return [func(value) for value in values]

def average_score(x):
    score = [a for b in x for a in b][1::2]
    return sum(score) / len(score)


if __name__ == "__main__":

    numbers = (2, 3, 8, 10)
    print(apply_to_list(square, numbers))
    print(apply_to_list(even, numbers))
    print(apply_to_list(factorial, numbers))

    sentence = "hello world, how are you?"
    print(sentence.title())

    scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
    print(average_score(scores))
