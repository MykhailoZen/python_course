import random
import string
from functools import reduce

# 1.Write a function that takes a list of numbers as input and returns a new list containing the square of each number
input_nums = random.sample(range(1, 20), 7)
print('Initial list:', input_nums)
square_nums = list(map(lambda x: x * x, input_nums))
print('Squared nums:', square_nums)

# 2.Write a function that takes a list of numbers as input and returns a new list containing only the even
even_nums = list(filter(lambda x: x % 2 == 0, input_nums))
print('Even nums:', even_nums)


# 3.Write a function that calculates the factorial of a number
def fact_of_n(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


value = input("Enter integer to get it's factorial:")
try:
    print(f'Factorial of {int(value)} is', fact_of_n(int(value)))
except:
    print('You have missed the chance to calculate factorial')

# 4.Capitalize the first letter of each word in a sentence "hello world, how are you?".
phrase = "hello world, how are you?"


def phrase_modifier(func):
    modified_phrase = func(phrase)
    print(modified_phrase)


def capitalizer(text):
    return string.capwords(text)


phrase_modifier(capitalizer)

# 5.Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]


def average_score(list_of_tuples):
    def int_only():
        return [x for row in list_of_tuples for x in row if type(x) == int]

    return sum(int_only()) / len(int_only())


print('Average score:', average_score(scores))
