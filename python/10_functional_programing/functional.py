# Practice - coding:
# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.
# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# Write a function that calculates the factorial of a number using the functional approach.
# Capitalize the first letter of each word in a sentence "hello world, how are you?".
# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take
# the list of tuples as input and return the average score.
from typing import List


def square(list_of_numbers: List[int]) -> List[int]:
    return [x **2 for x in list_of_numbers]

def even_numbers(list_of_numbers: List[int]) -> List[int]:
    return [x for x in list_of_numbers if x % 2 == 0]

def factorial(n: int) -> int:
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

def capitalize_each(word: str) -> str:
    return word.title()

def average_score(scoresarg: List[tuple[str, int]]) -> float:
    return sum([x[1] for x in scoresarg ])/len(scoresarg)


if __name__ == "__main__":
    print(square([4, 8, 1, 0]))
    print(even_numbers([5, 2, 9, 7]))
    print(factorial(8))
    print(capitalize_each("hello world, how are you?"))
    scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
    print(average_score(scores))
