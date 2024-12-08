# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.
# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# Write a function that calculates the factorial of a number using the functional approach.
# Capitalize the first letter of each word in a sentence "hello world, how are you?".
# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the
# list of tuples as input and return the average score.

from functools import reduce

numbers_1 = [1,2,3,4,5,8,12,44]
def square_numbers(numbers): return [x ** 2 for x in numbers]

def even_numbers(numbers): return[x for x in numbers if x % 2 == 0]

def factorial(n): return reduce(lambda x, y: x * y, range(1, n + 1))

s = "hello world, how are you?".title()

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
def average_score(student_scores):
    total_score = sum(score for _, score in student_scores)
    total_students = len(student_scores)
    return total_score / total_students


if __name__ == "__main__":
    print(square_numbers(numbers_1))
    print(even_numbers(numbers_1))
    print(factorial(5))
    print(s)
    print(average_score(scores))

