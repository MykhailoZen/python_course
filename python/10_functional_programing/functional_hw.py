# Practice - coding:
# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.
# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# Write a function that calculates the factorial of a number using the functional approach. (reduce lambda)
# Capitalize the first letter of each word in a sentence "hello world, how are you?". (return title(str))
# Given a list of students and their marks as tuples: (list(tuple)) + sum / len(list_of_students) = avg
#
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of
# tuples as input and return the average score.
from typing import List, Tuple
from functools import reduce


def square(list_integers: List[int]) -> List[int]:
    return [x ** 2 for x in list_integers]


def return_even(list_integers: List[int]) -> List[int]:
    return [x for x in list_integers if x % 2 == 0]


def factorial_of_num(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial_of_num(n - 1)


def factorial2_of_num(n: int) -> int:
    return reduce(lambda x, y: x * y, range(1, n + 1))


def capital(given_sentence: str) -> str:
    return given_sentence.title()


def avg_marks(list_of_students: List[Tuple[str, int]]) -> float:
    list_of_scores = []
    for x in list_of_students:
        list_of_scores.append(x[1])
    return sum(list_of_scores) / len(list_of_students)


if __name__ == '__main__':
    print(square([2, 4, 6]))
    print(return_even([3, 41, 60, 52, ]))
    print(capital("hello world, how are you?"))
    print(factorial_of_num(11))
    print(factorial2_of_num(11))
    print(avg_marks([("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]))
