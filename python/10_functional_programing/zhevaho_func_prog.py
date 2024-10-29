from math import factorial

# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.

list1 = [2,3,4]
list2 = [num ** 2 for num in list1]
print(list2)

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
even_list = [num for num in list1 if num%2 == 0]
print(even_list)

# Write a function that calculates the factorial of a number using the functional approach.

def calc_factorial(num):
    fact = 1
    for num in range (1, num +1):
        fact *= num
    return fact

print(calc_factorial(6))

# Capitalize the first letter of each word in a sentence "hello world, how are you?"

sentence = "hello world, how are you?"

capitalized = [word.capitalize() for word in sentence.split()]
def func(lis):
    return ' '.join(lis)

print(func(capitalized))

# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of
# tuples as input and return the average score.

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

def calc_average_score(lis):
    res = 0
    for student in lis:
        res += student[1]
    return res/len(lis)

print(calc_average_score(scores))