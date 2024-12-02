# 1) Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.
# 2) Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# 3) Write a function that calculates the factorial of a number using the functional approach.
# 4) Capitalize the first letter of each word in a sentence "hello world, how are you?".
# 5) Given a list of students and their marks as tuples:
#
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of
# tuples as input and return the average score.
from functools import reduce
from typing import List, Tuple


def square(list_of_numbers: List[int]) -> List[int]:
    return [number**2 for number in list_of_numbers]


def even_numbers(list_of_numbers: List[int]) -> List[int]:
    return [number for number in list_of_numbers if number % 2 == 0]


def factorial(number: int) -> int:
    return reduce(lambda x, y: x * y, range(1, number + 1))


def capitalize(string_for_capitalize: str) -> str:
    return string_for_capitalize.title()


def average_score(list_of_students: List[Tuple[str, int]]) -> float:
    return reduce(
        lambda x, y: x + y, [student[1] for student in list_of_students]
    ) / len(list_of_students)


if __name__ == "__main__":
    print(f"New list containing the square of each number {square([2, 6, 8, 4])}")
    print(f"New list containing only the even numbers {even_numbers([3, 6, 7, 4])}")
    n = 3
    print(f"Factorial of {n} = {factorial(n)}")
    str_to_capitalize = "hello world, how are you?"
    print(f"Capitalize the first letter of each word: {capitalize(str_to_capitalize)}")
    scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
    print(f"Average score of the students {average_score(scores)}")
