# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.
# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# Write a function that calculates the factorial of a number using the functional approach.
# Capitalize the first letter of each word in a sentence "hello world, how are you?".
# Given a list of students and their marks as tuples:
#
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the
# list of tuples as input and return the average score.
from functools import reduce
from typing import List, Tuple


def square_calculate(number_list: List[int]) -> List[int]:
    return [x ** 2 for x in number_list]


def even_numbers(number_list: List[int]) -> List[int]:
    return [x for x in number_list if x % 2 == 0]


def factorial_calculate(n: int) -> int:
    return reduce(lambda x, y: x * y, range(1, n + 1))


def capitalize_str(str_for_capitalize: str) -> str:
    return str_for_capitalize.title()


def average_score(student_list: List[Tuple[str, int]]) -> float:
    return sum([score[1] for score in student_list]) / len(student_list)


if __name__ == "__main__":
    print(f'List of square numbers {square_calculate([2, 3, 4, 5])}')
    print(f'List of even numbers {even_numbers([2, 3, 4, 5])}')
    n = 10
    print(f'Factorial number of {n} is {factorial_calculate(n)}')
    print(capitalize_str("hello world, how are you?"))
    print(average_score([("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]))